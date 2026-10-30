### fxmd_cot

Get CFTC Commitment of Traders (COT) data

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "type": "object",
  "properties": {
    "currency": {
      "type": "string",
      "title": "Currency",
      "enum": [
        "AUD",
        "CAD",
        "CHF",
        "EUR",
        "GBP",
        "JPY",
        "NZD",
        "USD",
        "XAU"
      ],
      "example": "AUD",
      "description": "Required path parameter. Allowed values: AUD, CAD, CHF, EUR, GBP, JPY, NZD, USD, XAU."
    },
    "start_date": {
      "type": "string",
      "description": "Optional query parameter. Start date YYYY-MM-DD",
      "examples": [
        "2025-09-01"
      ],
      "title": "Start Date"
    },
    "end_date": {
      "type": "string",
      "description": "Optional query parameter. End date YYYY-MM-DD",
      "examples": [
        "2026-03-01"
      ],
      "title": "End Date"
    },
    "limit": {
      "type": "integer",
      "maximum": 100,
      "minimum": 1,
      "description": "Optional query parameter. Maximum rows to return. Defaults to 20. Maximum 100.",
      "examples": [
        20
      ],
      "default": 20,
      "title": "Limit"
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Optional query parameter. Number of rows to skip after most-recent-first ordering.",
      "examples": [
        0
      ],
      "default": 0,
      "title": "Offset"
    },
    "page": {
      "anyOf": [
        {
          "type": "integer",
          "minimum": 1
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. One-based page number. When supplied, it takes precedence over offset.",
      "examples": [
        1
      ],
      "title": "Page"
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
      "description": "Optional query parameter. CFTC report type. `legacy_futures` (default): Legacy Futures-Only report with commercial / non-commercial / non-reportable positions. `legacy_combined`: the same categories from the futures-and-options combined report. `tff_futures` / `tff_combined`: Traders in Financial Futures report with dealer, asset manager, leveraged funds, other reportable and non-reportable long / short / spreading positions (FX contracts and the dollar index; not gold). `disaggregated_futures`: producer/merchant, swap dealer, managed money and other reportable positions (COMEX gold only). Each report adds the matching `*_net` and `*_zscore` columns.",
      "examples": [
        "legacy_futures",
        "tff_futures"
      ],
      "enum": [
        "legacy_futures",
        "legacy_combined",
        "tff_futures",
        "tff_combined",
        "disaggregated_futures"
      ],
      "default": "legacy_futures",
      "title": "Report"
    }
  },
  "required": [
    "currency"
  ],
  "additionalProperties": false
}
```
