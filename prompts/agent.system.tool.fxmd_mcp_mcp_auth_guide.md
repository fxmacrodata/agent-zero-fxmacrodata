### fxmd_mcp_mcp_auth_guide

Explains which authentication mode suits FXMacroData MCP across major clients and platforms: OAuth, an API key, or a bearer token, for ChatGPT/OpenAI Apps, Claude/Anthropic, Microsoft/VS Code/Copilot-style clients, AstrBot, Cursor, Codex, local scripts, and CI.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {},
  "type": "object",
  "title": "mcp_auth_guideArguments"
}
```
