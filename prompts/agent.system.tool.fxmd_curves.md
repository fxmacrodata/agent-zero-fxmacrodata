### fxmd_curves

Get curve analytics by currency

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "type": "object",
  "properties": {
    "currency": {
      "type": "string",
      "description": "Required path parameter. Currency code Allowed values: AUD, CAD, CHF, CNH, CNY, DKK, EUR, GBP, ILS, JPY, KRW, MYR, NOK, NZD, PEN, SEK, THB, USD.",
      "examples": [
        "GBP"
      ],
      "title": "Currency",
      "enum": [
        "AUD",
        "CAD",
        "CHF",
        "CNH",
        "CNY",
        "DKK",
        "EUR",
        "GBP",
        "ILS",
        "JPY",
        "KRW",
        "MYR",
        "NOK",
        "NZD",
        "PEN",
        "SEK",
        "THB",
        "USD"
      ],
      "example": "AUD"
    },
    "curve_family": {
      "type": "string",
      "description": "Optional query parameter. Official curve family to return. Allowed values: government_nominal.",
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
    "metric": {
      "type": "string",
      "description": "Optional query parameter. Curve metric to return. Allowed values: spot.",
      "examples": [
        "spot"
      ],
      "default": "spot",
      "title": "Metric",
      "enum": [
        "spot"
      ],
      "example": "spot"
    },
    "view": {
      "type": "string",
      "description": "Optional query parameter. Curve view to return: nodes, slopes, or forwards. Allowed values: nodes, slopes, forwards.",
      "examples": [
        "nodes",
        "slopes",
        "forwards"
      ],
      "default": "nodes",
      "title": "View",
      "enum": [
        "nodes",
        "slopes",
        "forwards"
      ],
      "example": "nodes"
    },
    "method": {
      "type": "string",
      "description": "Optional query parameter. Forward derivation method used when view=forwards. Allowed values: derived_from_spot_nodes.",
      "examples": [
        "derived_from_spot_nodes"
      ],
      "default": "derived_from_spot_nodes",
      "title": "Method",
      "enum": [
        "derived_from_spot_nodes"
      ],
      "example": "derived_from_spot_nodes"
    },
    "date": {
      "type": "string",
      "description": "Optional query parameter. Optional target date YYYY-MM-DD. The endpoint returns the latest available node per maturity up to this date, using a recent lookback window.",
      "examples": [
        "2026-06-01"
      ],
      "title": "Date"
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
    },
    "max_staleness_days": {
      "anyOf": [
        {
          "type": "integer",
          "maximum": 366,
          "minimum": 0
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Maximum reference-date age; defaults to 7 with as_of, otherwise 60.",
      "title": "Max Staleness Days"
    },
    "require_common_date": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Require all populated curve nodes to share a reference date; defaults true with as_of.",
      "title": "Require Common Date"
    }
  },
  "required": [
    "currency"
  ],
  "additionalProperties": false
}
```
