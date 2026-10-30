### fxmd_forex

Get FX spot rates

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "type": "object",
  "properties": {
    "base": {
      "type": "string",
      "description": "Required path parameter. Base currency code Allowed values: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "AUD"
      ],
      "title": "Base",
      "enum": [
        "AUD",
        "BRL",
        "CAD",
        "CHF",
        "CNH",
        "CNY",
        "DKK",
        "EUR",
        "GBP",
        "HUF",
        "ILS",
        "JPY",
        "KRW",
        "MYR",
        "NGN",
        "NOK",
        "NZD",
        "PEN",
        "SEK",
        "THB",
        "TWD",
        "USD"
      ],
      "example": "AUD"
    },
    "quote": {
      "type": "string",
      "description": "Required path parameter. Quote currency code Allowed values: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "USD"
      ],
      "title": "Quote",
      "enum": [
        "AUD",
        "BRL",
        "CAD",
        "CHF",
        "CNH",
        "CNY",
        "DKK",
        "EUR",
        "GBP",
        "HUF",
        "ILS",
        "JPY",
        "KRW",
        "MYR",
        "NGN",
        "NOK",
        "NZD",
        "PEN",
        "SEK",
        "THB",
        "TWD",
        "USD"
      ],
      "example": "AUD"
    },
    "start_date": {
      "type": "string",
      "description": "Optional query parameter. Start date YYYY-MM-DD",
      "examples": [
        "2026-01-01"
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
    "indicators": {
      "type": "string",
      "description": "Optional query parameter. Comma-separated technical indicators to compute (e.g. sma_20,rsi_14,macd,bollinger_bands). Use 'all' to request every supported indicator.",
      "examples": [
        "sma_20,rsi_14,macd"
      ],
      "title": "Indicators"
    },
    "dataset_version": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Pin the content version returned by the first page; changed history returns 409.",
      "title": "Dataset Version"
    }
  },
  "required": [
    "base",
    "quote"
  ],
  "additionalProperties": false
}
```
