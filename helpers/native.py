"""Native Agent Zero dispatch and application-owned configuration."""

from __future__ import annotations

import os
import re

from helpers.plugins import get_plugin_config
from helpers.tool import Response, Tool
from pydantic import SecretStr

from usr.plugins.fxmacrodata.helpers.runtime import (
    FXMacroDataSettings,
    RequestFailure,
    Runtime,
)


def settings_for(agent) -> FXMacroDataSettings:
    config = get_plugin_config("fxmacrodata", agent=agent) or {}
    variable = config.get("api_key_env", "FXMACRODATA_API_KEY")
    if not isinstance(variable, str) or not re.fullmatch(r"[A-Z_][A-Z0-9_]{0,63}", variable):
        raise RequestFailure("Set a valid API key environment-variable name in plugin settings.")
    value = os.getenv(variable, "")
    if not value and variable == "FXMACRODATA_API_KEY":
        value = os.getenv("FXMD_API_KEY", "")
    try:
        return FXMacroDataSettings(
            api_key=SecretStr(value),
            request_timeout_seconds=config.get("request_timeout_seconds", 30),
            tool_timeout_seconds=config.get("tool_timeout_seconds", 90),
            max_concurrency=1,
        )
    except Exception:
        raise RequestFailure("Check the request timeout settings in FXMacroData configuration.") from None


class PublicTool(Tool):
    """A native tool with a fixed operation selected by its installed module."""

    operation: str

    async def execute(self, **kwargs) -> Response:
        try:
            async with Runtime(settings_for(self.agent), operations=[self.operation]) as runtime:
                result = await runtime.execute(self.operation, kwargs)
            return Response(
                message=result.model_dump_json(),
                break_loop=False,
                additional={"fxmacrodata": result.model_dump(mode="json")},
            )
        except RequestFailure as exc:
            return Response(message=str(exc), break_loop=False)

    async def before_execution(self, **kwargs):
        # Model-supplied values may contain sensitive text; omit them from logs.
        original_args = self.args
        try:
            self.args = {}
            await super().before_execution(**kwargs)
        finally:
            self.args = original_args
