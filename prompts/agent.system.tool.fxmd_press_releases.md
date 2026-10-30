### fxmd_press_releases

Recent central bank press releases

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
        "BRL",
        "CAD",
        "CHF",
        "DKK",
        "EUR",
        "GBP",
        "ILS",
        "JPY",
        "NGN",
        "NOK",
        "NZD",
        "PEN",
        "SEK",
        "USD"
      ],
      "example": "AUD",
      "description": "Required path parameter. Allowed values: AUD, BRL, CAD, CHF, DKK, EUR, GBP, ILS, JPY, NGN, NOK, NZD, PEN, SEK, USD."
    },
    "limit": {
      "type": "integer",
      "maximum": 50,
      "minimum": 1,
      "description": "Optional query parameter. Maximum number of press releases to return",
      "examples": [
        10
      ],
      "default": 20,
      "title": "Limit"
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Optional query parameter. Zero-based offset into the full press-release feed before pagination.",
      "default": 0,
      "title": "Offset"
    }
  },
  "required": [
    "currency"
  ],
  "additionalProperties": false
}
```
