"""Native Tool execution through actual client; synthetic offline HTTP only."""
import asyncio,importlib,json,os,sys,types
from pathlib import Path
from unittest.mock import patch

import pytest,requests,yaml
from helpers.tool import Tool,Response
from helpers.print_style import PrintStyle
from usr.plugins.fxmacrodata.helpers import native
from usr.plugins.fxmacrodata.helpers.runtime import Runtime,FXMacroDataClient,FXMacroDataSettings,RequestFailure
from usr.plugins.fxmacrodata.helpers.public_client import list_operations,FXMacroDataError
from transport_fixtures import Transport,arguments,PAYLOAD

OPS=list_operations();ROOT=Path(native.__file__).parents[1]

def run(coro):return asyncio.run(coro)

def tool_for(op,**kwargs):
    cls=importlib.import_module("usr.plugins.fxmacrodata.tools.fxmd_"+op.name).FXMacroDataTool
    assert issubclass(cls,Tool)
    return cls(agent=types.SimpleNamespace(),name="fxmd_"+op.name,method=None,args=kwargs,message="",loop_data=None)

@pytest.mark.parametrize("operation",OPS,ids=lambda op:op.name)
@pytest.mark.parametrize("key",["","synthetic-agentzero-key"])
def test_all_native_tools_real_client(operation,key,monkeypatch):
    monkeypatch.setenv("FXMACRODATA_API_KEY",key);monkeypatch.delenv("FXMD_API_KEY",raising=False)
    transport=Transport();args=arguments(operation)
    with patch.object(requests.Session,"request",lambda session,*a,**kw:transport.request(session,*a,**kw)):
        result=run(tool_for(operation).execute(**args))
    assert isinstance(result,Response) and result.break_loop is False
    assert result.additional is not None,result.message
    value=json.loads(result.message);assert value==result.additional["fxmacrodata"]
    assert value["operation"]==operation.name
    assert "native-host-test" in result.message
    if operation.name=="stream_events":
        assert value["data"]["events"][0]["data"]["data"][0]["value"] is None
        assert value["data"]["capture_complete"] is True
    else:
        assert value["records"][0]["value"] is None
    assert value["source_url"].startswith("https://")
    assert transport.calls and all(r.closed for r in transport.responses)
    for method,url,request in transport.calls:
        assert not any(k.lower() in {"api_key","authorization","access_token"} for k in (request.get("params") or {}))
        assert request["allow_redirects"] is False
        if key:
            expected="Authorization" if "mcp.fxmacrodata.com" in url else "X-API-Key"
            assert request["headers"][expected]==("Bearer "+key if expected=="Authorization" else key)
        assert key=="" or key not in result.message
    if operation.name=="research_panel":
        request=next(c for c in transport.calls if c[0]=="POST")[2]
        assert request["json"]==args["body"]

def test_inventory_prompts_and_schemas_match_native_modules():
    assert len(OPS)==98 and sum(op.method=="MCP" for op in OPS)==57
    assert len(list((ROOT/"tools").glob("fxmd_*.py")))==98
    for op in OPS:
        text=(ROOT/"prompts"/("agent.system.tool.fxmd_"+op.name+".md")).read_text()
        schema=json.loads(text.split("```json\n",1)[1].split("```",1)[0])
        assert schema==op.input_schema

@pytest.mark.parametrize("reserved",["api_key","authorization","access_token","url","base_url"])
def test_model_arguments_cannot_supply_secrets_or_endpoints(reserved):
    result=run(tool_for(OPS[0]).execute(**{reserved:"synthetic-secret"}))
    assert result.additional is None and "synthetic-secret" not in result.message

@pytest.mark.parametrize("status",[302,401,403,404,429,500])
def test_errors_are_not_successful_data_and_do_not_leak_keys(status,monkeypatch):
    monkeypatch.setenv("FXMACRODATA_API_KEY","synthetic-key")
    op=next(op for op in OPS if op.name=="data_catalogue");transport=Transport(status=status)
    with patch.object(requests.Session,"request",lambda session,*a,**kw:transport.request(session,*a,**kw)):
        result=run(tool_for(op).execute(currency="usd"))
    assert result.additional is None
    assert "synthetic-key" not in result.message and "http" not in result.message.lower()

def test_structured_and_escaped_mcp_credentials_redacted(monkeypatch):
    monkeypatch.setenv("FXMACRODATA_API_KEY","synthetic-key")
    value={"content":[{"type":"text","text":json.dumps({"api_key":"synthetic-key","x":"synthetic-key"})},{"type":"resource","resource":{"uri":"ui://fxmacrodata/example","mimeType":"text/html","text":"<p>example</p>"}}]}
    transport=Transport(payload=value);op=next(op for op in OPS if op.name=="mcp_mcp_capabilities")
    with patch.object(requests.Session,"request",lambda session,*a,**kw:transport.request(session,*a,**kw)):
        result=run(tool_for(op).execute())
    assert result.additional and "synthetic-key" not in result.message
    assert "ui://fxmacrodata/example" in result.message

def test_public_mode_does_not_inherit_legacy_key_when_custom_empty_variable(monkeypatch):
    monkeypatch.setenv("FXMD_API_KEY","unwanted-synthetic")
    monkeypatch.delenv("PUBLIC_ONLY_TEST",raising=False)
    with patch.object(native,"get_plugin_config",return_value={"api_key_env":"PUBLIC_ONLY_TEST"}):
        assert native.settings_for(None).api_key.get_secret_value()==""

def test_config_serialization_never_contains_key():
    settings=FXMacroDataSettings(api_key="synthetic-private-key")
    assert "synthetic-private-key" not in repr(settings)+settings.model_dump_json()
    assert "synthetic-private-key" not in repr(Runtime(settings))

def test_before_execution_does_not_log_model_values():
    op=OPS[0];tool=tool_for(op);tool.args={"untrusted":"synthetic-model-secret"}
    seen=[]
    tool.agent=types.SimpleNamespace(agent_name="Test",context=types.SimpleNamespace(log=types.SimpleNamespace(log=lambda **kw:seen.append(kw))))
    PrintStyle.lines.clear();run(tool.before_execution())
    assert seen[0]["kvps"]=={}
    assert tool.args["untrusted"]=="synthetic-model-secret"
    assert "synthetic-model-secret" not in repr(seen)+repr(PrintStyle.lines)

def test_schema_failure_happens_before_http():
    op=next(op for op in OPS if op.name=="data_catalogue")
    with patch.object(requests.Session,"request",side_effect=AssertionError("network")):
        result=run(tool_for(op).execute(currency=123))
    assert result.additional is None

def test_http200_error_body_is_not_successful_data():
    transport=Transport(payload={"error":"api_key_required","detail":"synthetic-private-detail"})
    with patch.object(requests.Session,"request",lambda session,*a,**kw:transport.request(session,*a,**kw)):
        result=run(tool_for(OPS[0]).execute())
    assert result.additional is None
    assert "synthetic-private-detail" not in result.message

@pytest.mark.parametrize("value",[float("nan"),float("inf")])
def test_nonfinite_json_rejected_before_transport(value):
    op=next(op for op in OPS if op.name=="data_catalogue")
    with patch.object(requests.Session,"request",side_effect=AssertionError("network")):
        result=run(tool_for(op).execute(currency=value))
    assert result.additional is None

def test_transport_exception_is_sanitized():
    with patch.object(requests.Session,"request",side_effect=requests.ConnectionError("synthetic-secret")):
        result=run(tool_for(OPS[0]).execute())
    assert result.additional is None and "synthetic-secret" not in result.message

def test_runtime_cancellation_does_not_wait_for_synchronous_request():
    import threading
    started=threading.Event();release=threading.Event();closed=threading.Event()
    class Client:
        def __init__(self,**kwargs):pass
        def execute(self,*args):
            started.set();release.wait(2)
            return types.SimpleNamespace(as_dict=lambda:{"operation":"health","data":{},"records":[],"source_url":"https://fxmacrodata.com"})
        def close(self):closed.set()
    async def scenario():
        async with Runtime(client_factory=Client) as runtime:
            task=asyncio.create_task(runtime.execute("health",{}))
            while not started.is_set():await asyncio.sleep(.001)
            task.cancel()
            with pytest.raises(asyncio.CancelledError):await asyncio.wait_for(task,.2)
        release.set()
    try:run(scenario())
    finally:release.set()
    assert closed.wait(1)

def test_read_only_lifecycle_is_idempotent_and_never_installs():
    import importlib.util
    spec=importlib.util.spec_from_file_location("fxmd_hooks",ROOT/"hooks.py");hooks=importlib.util.module_from_spec(spec);spec.loader.exec_module(hooks)
    with patch("subprocess.run",side_effect=AssertionError("no package manager")),patch.object(requests.Session,"request",side_effect=AssertionError("no network")):
        hooks.install();hooks.install();hooks.uninstall()
    assert not (ROOT/"execute.py").exists()

def test_lifecycle_missing_dependency_is_explicit():
    import importlib.util,importlib.metadata
    spec=importlib.util.spec_from_file_location("fxmd_hooks",ROOT/"hooks.py");hooks=importlib.util.module_from_spec(spec);spec.loader.exec_module(hooks)
    with patch.object(hooks.metadata,"version",side_effect=importlib.metadata.PackageNotFoundError):
        with pytest.raises(RuntimeError,match="No dependency changes"):hooks.install()

def test_manifest_has_only_names_and_runtime_paths():
    manifest=yaml.safe_load((ROOT/"plugin.yaml").read_text());assert manifest["name"]=="fxmacrodata" and manifest["version"]=="0.2.0"
    config=yaml.safe_load((ROOT/"default_config.yaml").read_text());assert config["api_key_env"]=="FXMACRODATA_API_KEY"
    assert "api_key" not in config
