"""Bounded execution of the documented FXMacroData public client."""

from __future__ import annotations

import asyncio
import json
import os
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from typing import Any, Callable

from .public_client import FXMacroDataClient as _PublicClient, FXMacroDataError, list_operations
from .response_safety import sanitize_response


class FXMacroDataClient(_PublicClient):
    """Redact structured MCP text before projecting records."""

    def _safe(self, value):
        return sanitize_response(value, self._api_key)
from jsonschema import Draft202012Validator
from pydantic import BaseModel, ConfigDict, Field, JsonValue, SecretStr
from referencing import Registry


class FXMacroDataSettings(BaseModel):
    """Application-owned credentials and request limits."""

    model_config = ConfigDict(frozen=True, extra="forbid", hide_input_in_errors=True)
    api_key: SecretStr = Field(
        default_factory=lambda: SecretStr(
            os.getenv("FXMACRODATA_API_KEY") or os.getenv("FXMD_API_KEY") or ""
        ),
        exclude=True,
        repr=False,
    )
    request_timeout_seconds: float = Field(default=30, ge=1, le=120, allow_inf_nan=False)
    tool_timeout_seconds: float = Field(default=90, ge=1, le=600, allow_inf_nan=False)
    max_concurrency: int = Field(default=4, ge=1, le=32, strict=True)


class FXMacroDataResult(BaseModel):
    """The unchanged public payload, record view and provenance."""

    model_config = ConfigDict(frozen=True, extra="forbid", strict=True)
    operation: str
    data: JsonValue
    records: list[dict[str, JsonValue]]
    source_url: str


class RequestFailure(Exception):
    """A public, input-free failure suitable for a tool result."""


def _failure(exc: Exception) -> str:
    if isinstance(exc, FXMacroDataError):
        detail = str(exc).lower()
        if "authorized" in detail:
            return "Check your configured FXMacroData API key and subscription access."
        if "rate limit" in detail:
            return "FXMacroData rate limit reached. Retry later."
        if "timeout" in detail or "budget" in detail:
            return "FXMacroData request limits were reached. Retry later."
        if "unavailable" in detail:
            return "The requested resource is unavailable. Check catalogue discovery."
    return "FXMacroData request failed. Check subscription access, filters and connectivity."


class Runtime:
    """An explicit context owns the worker pool; each call owns its HTTP client."""

    def __init__(
        self,
        settings: FXMacroDataSettings | None = None,
        *,
        operations: list[str] | tuple[str, ...] | None = None,
        include_mcp: bool = True,
        client_factory: Callable[..., Any] | None = None,
    ):
        self.settings = settings if settings is not None else FXMacroDataSettings()
        inventory = {op.name: op for op in list_operations(include_mcp=include_mcp)}
        if operations is not None:
            if not operations or len(set(operations)) != len(operations):
                raise ValueError("Select at least one operation without duplicates.")
            if any(name not in inventory for name in operations):
                raise ValueError("Unknown or disabled FXMacroData operation.")
            inventory = {name: inventory[name] for name in operations}
        self.operations = deepcopy(inventory)
        self._factory = client_factory or FXMacroDataClient
        self._executor: ThreadPoolExecutor | None = None

    def __repr__(self) -> str:
        return f"Runtime(operations={len(self.operations)})"

    async def __aenter__(self):
        if self._executor is not None:
            raise RuntimeError("FXMacroData context is already open.")
        self._executor = ThreadPoolExecutor(
            max_workers=self.settings.max_concurrency, thread_name_prefix="fxmacrodata"
        )
        return self

    async def __aexit__(self, *args):
        executor, self._executor = self._executor, None
        if executor is not None:
            executor.shutdown(wait=False, cancel_futures=True)

    def validate(self, name: str, arguments: Any) -> dict[str, Any]:
        if name not in self.operations:
            raise RequestFailure("Unknown or disabled FXMacroData operation.")
        if not isinstance(arguments, dict) or any(not isinstance(k, str) for k in arguments):
            raise RequestFailure("Tool arguments must be an object with string keys.")
        reserved = {"api_key", "authorization", "access_token", "url", "base_url"}
        if any(key.lower() in reserved for key in arguments):
            raise RequestFailure("Configure credentials in the application, not tool arguments.")
        try:
            value = json.loads(json.dumps(arguments, allow_nan=False))
            Draft202012Validator(
                self.operations[name].input_schema, registry=Registry()
            ).validate(value)
            return value
        except Exception:
            raise RequestFailure("Arguments do not match this tool's input schema.") from None

    def _execute(self, name: str, arguments: dict[str, Any]) -> FXMacroDataResult:
        client = None
        try:
            client = self._factory(
                api_key=self.settings.api_key.get_secret_value(),
                timeout=self.settings.request_timeout_seconds,
            )
            result = client.execute(name, arguments)
            payload = result.payload
            if isinstance(payload, dict) and (payload.get("error") or payload.get("status") == "error"):
                raise FXMacroDataError("The requested resource is unavailable. Check access and arguments.")
            return FXMacroDataResult.model_validate(result.as_dict())
        except Exception as exc:
            raise RequestFailure(_failure(exc)) from None
        finally:
            if client is not None:
                try:
                    client.close()
                except Exception:
                    pass

    async def execute(self, name: str, arguments: dict[str, Any]) -> FXMacroDataResult:
        validated = self.validate(name, arguments)
        if self._executor is None:
            raise RequestFailure("Open the FXMacroData tools with an async context first.")
        future = self._executor.submit(self._execute, name, validated)
        try:
            return await asyncio.wait_for(
                asyncio.wrap_future(future), timeout=self.settings.tool_timeout_seconds
            )
        except asyncio.TimeoutError:
            raise RequestFailure("FXMacroData tool deadline exceeded. Retry later.") from None
