### fxmd_mcp_macro_factor

Return a precomputed macro factor for one currency, with optional stored component scores and source references. The factor is a documented summary value and does not replace the underlying macro releases. Access: USD is available without an API key; every other currency returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "currency": {
      "description": "3-letter ISO currency code (case-insensitive).",
      "examples": [
        "usd",
        "eur",
        "gbp",
        "jpy"
      ],
      "type": "string"
    },
    "factor": {
      "description": "Factor slug, for example monetary_stance.",
      "examples": [
        "monetary_stance"
      ],
      "type": "string"
    },
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional inclusive start date, YYYY-MM-DD."
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional inclusive end date, YYYY-MM-DD."
    },
    "include_components": {
      "default": false,
      "description": "Include stored component scores when available.",
      "type": "boolean"
    },
    "include_sources": {
      "default": false,
      "description": "Include public source endpoint references when available.",
      "type": "boolean"
    },
    "limit": {
      "default": 20,
      "description": "Maximum rows to return.",
      "maximum": 100,
      "minimum": 1,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Zero-based row offset.",
      "minimum": 0,
      "type": "integer"
    }
  },
  "required": [
    "currency",
    "factor"
  ],
  "type": "object",
  "title": "macro_factorArguments"
}
```
