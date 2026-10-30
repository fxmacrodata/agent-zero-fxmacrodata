### fxmd_mcp_macro_news

Return recent official central-bank news and press-release headlines for a currency, covering central-bank policy, inflation, employment, GDP, trade, fiscal, energy, and commodity narratives. Rows are official-source headlines with lightweight keyword-derived affected_indicators and sentiment fields when a headline is classifiable. Supported currencies: AUD, BRL, CAD, CHF, DKK, EUR, GBP, ILS, JPY, NGN, NOK, NZD, PEN, SEK, USD. Access: USD is available without an API key; every other currency returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "currency": {
      "description": "3-letter ISO currency code (case-insensitive). Supported: AUD, BRL, CAD, CHF, DKK, EUR, GBP, ILS, JPY, NGN, NOK, NZD, PEN, SEK, USD.",
      "examples": [
        "usd",
        "eur",
        "gbp",
        "jpy"
      ],
      "type": "string"
    },
    "lookback_days": {
      "default": 7,
      "description": "Maximum age of returned headlines in calendar days when headline timestamps are available.",
      "examples": [
        7,
        30
      ],
      "maximum": 90,
      "minimum": 1,
      "type": "integer"
    },
    "limit": {
      "default": 20,
      "description": "Maximum number of headline rows to request.",
      "examples": [
        10,
        20
      ],
      "maximum": 50,
      "minimum": 1,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Zero-based headline offset.",
      "examples": [
        0
      ],
      "minimum": 0,
      "type": "integer"
    }
  },
  "required": [
    "currency"
  ],
  "type": "object",
  "title": "macro_newsArguments"
}
```
