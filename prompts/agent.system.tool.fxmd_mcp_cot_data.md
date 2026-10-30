### fxmd_mcp_cot_data

Get weekly CFTC Commitment of Traders (COT) positioning data for a currency's FX futures contract on the CME, covering speculator positioning, non-commercial longs vs shorts, hedge-fund FX positioning, and sentiment extremes. Returns weekly snapshots with long/short open interest by trader category. Updated every Friday at 15:30 ET reflecting the Tuesday cutoff. USD (the USD Index contract) is available without an API key for the most recent 90 days on a 15-minute release delay; every other currency and the full history need an API key. Supported currencies: AUD, CAD, CHF, EUR, GBP, JPY, NZD, USD, XAU. Access: USD is available without an API key; every other currency returns subscription_required with a subscribe link.

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
      "description": "CFTC report type. Omit for the Legacy futures-only report (commercial / non-commercial / non-reportable). One of: legacy_futures, legacy_combined, tff_futures, tff_combined, disaggregated_futures. TFF reports return dealer, asset manager, leveraged funds and other reportable positions for FX contracts and the dollar index; disaggregated_futures is published for XAU (COMEX gold) only.",
      "examples": [
        "tff_futures",
        "tff_combined",
        "legacy_combined"
      ]
    }
  },
  "required": [
    "currency"
  ],
  "type": "object",
  "title": "cot_dataArguments"
}
```
