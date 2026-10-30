### fxmd_mcp_market_sessions

Returns which FX trading sessions are currently open (Sydney, Tokyo, London, New York) and when the next session opens or closes, for questions such as 'is the market open?', 'when does London open?', or 'which sessions overlap right now?'. An ISO-8601 UTC timestamp in `at` returns the snapshot for a specific moment instead of now. Accounts for weekends and major banking holidays. Access: free, no API key required.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "at": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional ISO-8601 UTC timestamp; defaults to now. Use to snapshot session state at a specific moment.",
      "examples": [
        "2025-06-15T13:30:00Z",
        "2025-12-25T00:00:00Z"
      ]
    }
  },
  "type": "object",
  "title": "market_sessionsArguments"
}
```
