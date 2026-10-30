### fxmd_mcp_fx_intraday_reference_rates

Return subscriber intraday official FX reference-rate observations for one pair. Coverage is limited to the pairs and sources in the FX reference pair universe. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "base": {
      "description": "Base currency code.",
      "examples": [
        "eur"
      ],
      "type": "string"
    },
    "quote": {
      "description": "Quote currency code.",
      "examples": [
        "usd"
      ],
      "type": "string"
    },
    "start_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional inclusive RFC 3339 source timestamp.",
      "examples": [
        "2026-07-20T00:00:00Z"
      ]
    },
    "end_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional inclusive RFC 3339 source timestamp.",
      "examples": [
        "2026-07-21T00:00:00Z"
      ]
    }
  },
  "required": [
    "base",
    "quote"
  ],
  "type": "object",
  "title": "fx_intraday_reference_ratesArguments"
}
```
