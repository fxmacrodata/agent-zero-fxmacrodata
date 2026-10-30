### fxmd_rate_differentials

Get pair rate differentials

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
    "measure": {
      "type": "string",
      "description": "Optional query parameter. Shared rate measure to compare across the pair. Allowed values: auto, risk_free_rate, gov_bond_2y, gov_bond_10y, policy_rate.",
      "examples": [
        "auto",
        "risk_free_rate",
        "gov_bond_2y"
      ],
      "default": "auto",
      "title": "Measure",
      "enum": [
        "auto",
        "risk_free_rate",
        "gov_bond_2y",
        "gov_bond_10y",
        "policy_rate"
      ],
      "example": "auto"
    },
    "rate_type": {
      "type": "string",
      "description": "Optional query parameter. Differential type: spot for shared rate measures, forward for derived curve segments. Allowed values: spot, forward.",
      "examples": [
        "spot",
        "forward"
      ],
      "default": "spot",
      "title": "Rate Type",
      "enum": [
        "spot",
        "forward"
      ],
      "example": "spot"
    },
    "curve_family": {
      "type": "string",
      "description": "Optional query parameter. Curve family used when rate_type=forward. Allowed values: government_nominal.",
      "examples": [
        "government_nominal"
      ],
      "default": "government_nominal",
      "title": "Curve Family",
      "enum": [
        "government_nominal"
      ],
      "example": "government_nominal"
    },
    "start_tenor_years": {
      "type": "number",
      "description": "Optional query parameter. Start tenor in years when rate_type=forward.",
      "examples": [
        2.0
      ],
      "default": 2.0,
      "title": "Start Tenor Years"
    },
    "end_tenor_years": {
      "type": "number",
      "description": "Optional query parameter. End tenor in years when rate_type=forward.",
      "examples": [
        5.0
      ],
      "default": 5.0,
      "title": "End Tenor Years"
    },
    "start_date": {
      "type": "string",
      "description": "Optional query parameter. Inclusive start date YYYY-MM-DD. Defaults to 365 days ago.",
      "examples": [
        "2026-01-01"
      ],
      "title": "Start Date"
    },
    "end_date": {
      "type": "string",
      "description": "Optional query parameter. Inclusive end date YYYY-MM-DD. Defaults to today.",
      "examples": [
        "2026-06-01"
      ],
      "title": "End Date"
    },
    "limit": {
      "type": "integer",
      "maximum": 100,
      "minimum": 1,
      "description": "Optional query parameter. Maximum rows to return. Defaults to 20. Maximum 100.",
      "default": 20,
      "title": "Limit"
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Optional query parameter. Number of rows to skip after most-recent-first ordering.",
      "default": 0,
      "title": "Offset"
    },
    "as_of": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Explicit UTC information cutoff for verified vintage replay; date means start of day.",
      "title": "As Of"
    },
    "availability": {
      "type": "string",
      "pattern": "^(public|captured)$",
      "description": "Optional query parameter. Source-public or captured-value availability clock.",
      "default": "public",
      "title": "Availability"
    }
  },
  "required": [
    "base",
    "quote"
  ],
  "additionalProperties": false
}
```
