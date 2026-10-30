"""Host seam harness; actual Tool/Response source supplied explicitly offline."""
import importlib.util,os,sys,types
from pathlib import Path

class Dummy:
    pass

agent=types.ModuleType("agent");agent.Agent=Dummy;agent.LoopData=Dummy;sys.modules["agent"]=agent
helpers=types.ModuleType("helpers");helpers.__path__=[];sys.modules["helpers"]=helpers
extension=types.ModuleType("helpers.extension")
async def call_extensions_async(*args,**kwargs):
    return None
extension.call_extensions_async=call_extensions_async;sys.modules[extension.__name__]=extension
printer=types.ModuleType("helpers.print_style")
class PrintStyle:
    lines=[]
    def __init__(self,**kwargs):pass
    def print(self,value=""):self.lines.append(value)
    def stream(self,value=""):self.lines.append(value)
printer.PrintStyle=PrintStyle;sys.modules[printer.__name__]=printer
strings=types.ModuleType("helpers.strings");strings.sanitize_string=lambda value:value;sys.modules[strings.__name__]=strings
plugins=types.ModuleType("helpers.plugins");plugins.get_plugin_config=lambda name,agent=None:{};sys.modules[plugins.__name__]=plugins
tool_file=os.environ.get("FXMD_AGENTZERO_TOOL_SOURCE")
if not tool_file or not Path(tool_file).is_file():
    raise RuntimeError("Provide reviewed official helpers/tool.py via FXMD_AGENTZERO_TOOL_SOURCE; this harness does not fake the Tool base class.")
spec=importlib.util.spec_from_file_location("helpers.tool",tool_file)
tool=importlib.util.module_from_spec(spec);sys.modules[spec.name]=tool;spec.loader.exec_module(tool)
