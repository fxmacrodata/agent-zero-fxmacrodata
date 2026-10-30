### fxmd_mcp_data_catalogue

List every macroeconomic indicator FXMacroData publishes for a currency, with units, frequency, and coverage/freshness metadata. Returns the exact `indicator` slug strings used across FXMacroData indicator, calendar, and prediction endpoints. Rows whose `coverage` is stale, partial, or unavailable are not suitable for real-time carry or inflation analysis. Supported currencies (lowercase 3-letter codes): AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD. Access: free for every currency, no API key required.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "currency": {
      "description": "3-letter ISO currency code (case-insensitive). Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "usd",
        "eur",
        "gbp",
        "jpy"
      ],
      "type": "string"
    },
    "include_coverage": {
      "default": true,
      "description": "Include coverage/freshness rows with latest_available_date, coverage_quality, has_recent_data, and recent_observation_count. These rows show whether an indicator series is current enough for analysis.",
      "examples": [
        true
      ],
      "type": "boolean"
    },
    "include_capabilities": {
      "default": false,
      "description": "Include machine-readable indicator capabilities when the API supports them, such as supported transformations, history availability, and release-calendar linkage.",
      "examples": [
        false
      ],
      "type": "boolean"
    },
    "indicator": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional indicator slug that narrows the result to that one catalogue entry and its coverage row, for example `core_inflation`. Useful when the candidate series is already known; omit it to list every indicator.",
      "examples": [
        "core_inflation"
      ]
    }
  },
  "required": [
    "currency"
  ],
  "type": "object",
  "title": "data_catalogueArguments"
}
```
