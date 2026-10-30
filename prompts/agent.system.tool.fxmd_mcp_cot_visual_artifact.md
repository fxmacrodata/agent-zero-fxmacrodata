### fxmd_mcp_cot_visual_artifact

Returns weekly CFTC COT positioning data with MCP Apps chart metadata. By default it charts noncommercial net positioning; the `metric` parameter selects another COT field. Access: USD is available without an API key; every other currency returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "currency": {
      "description": "3-letter ISO currency code for the FX futures contract (case-insensitive). Supported: AUD, CAD, CHF, EUR, GBP, JPY, NZD, USD, XAU.",
      "examples": [
        "eur",
        "jpy",
        "gbp",
        "aud"
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
      "description": "Inclusive lower bound, YYYY-MM-DD.",
      "examples": [
        "2020-01-01",
        "2024-06-30"
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
      "description": "Inclusive upper bound, YYYY-MM-DD.",
      "examples": [
        "2020-01-01",
        "2024-06-30"
      ]
    },
    "metric": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "noncommercial_net",
      "description": "Field to plot from each COT row. Typical values: noncommercial_net, noncommercial_net_zscore, noncommercial_long, noncommercial_short, open_interest.",
      "examples": [
        "noncommercial_net",
        "noncommercial_net_zscore",
        "noncommercial_long",
        "open_interest"
      ]
    },
    "report": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CFTC report type; omit for the Legacy futures-only report. One of: legacy_futures, legacy_combined, tff_futures, tff_combined, disaggregated_futures. With a TFF report, plot a TFF metric such as leveraged_funds_net or asset_manager_net.",
      "examples": [
        "tff_futures"
      ]
    }
  },
  "required": [
    "currency"
  ],
  "type": "object",
  "title": "cot_visual_artifactArguments"
}
```
