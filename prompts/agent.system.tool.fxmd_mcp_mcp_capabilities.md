### fxmd_mcp_mcp_capabilities

Explains what the FXMacroData MCP server can do: which tools render MCP Apps, which return plain rows, what is public versus subscriber-only, and how tool selection differs across ChatGPT, Claude, Cursor, Codex, and plain MCP clients. Suited to questions about what is available, why visuals are not showing, or how to get the same result in a different interface.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {},
  "type": "object",
  "title": "mcp_capabilitiesArguments"
}
```
