### fxmd_mcp_seasonality

Get monthly return seasonality for an FX pair or XAU/USD, covering seasonal patterns, month-of-year tendency, historical monthly win rate, and XAUUSD/gold seasonality. Returns monthly average return, median return, win rate, sample size, dispersion, and per-year monthly returns from stored FX or gold series. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "instrument": {
      "description": "Six-letter pair such as EURUSD, AUDUSD, USDJPY, or XAUUSD. Slashes and separators are accepted by the REST endpoint only when passed as a single string.",
      "examples": [
        "XAUUSD",
        "EURUSD",
        "AUDUSD"
      ],
      "type": "string"
    },
    "lookback_years": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 10,
      "description": "Number of years to include, 2-30. Defaults to 10.",
      "examples": [
        10
      ]
    },
    "month": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional month filter, 1-12 or name such as July.",
      "examples": [
        "July"
      ]
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
      "description": "Inclusive upper bound, YYYY-MM-DD. Defaults to today.",
      "examples": [
        "2020-01-01",
        "2024-06-30"
      ]
    }
  },
  "required": [
    "instrument"
  ],
  "type": "object",
  "title": "seasonalityArguments"
}
```
