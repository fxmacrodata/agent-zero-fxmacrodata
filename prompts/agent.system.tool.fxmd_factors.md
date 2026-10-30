### fxmd_factors

Get a precomputed FX factor for one currency

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
        "USD"
      ],
      "example": "AUD",
      "description": "Required path parameter. Allowed values: AUD, CAD, CHF, EUR, GBP, JPY, NZD, USD."
    },
    "factor": {
      "type": "string",
      "description": "Required path parameter. Factor slug, for example monetary_stance. Allowed values: monetary_stance.",
      "examples": [
        "monetary_stance"
      ],
      "title": "Factor",
      "enum": [
        "monetary_stance"
      ],
      "example": "monetary_stance"
    },
    "start_date": {
      "type": "string",
      "description": "Optional query parameter. Inclusive start date YYYY-MM-DD. With no dates, returns latest only.",
      "examples": [
        "2026-01-01"
      ],
      "title": "Start Date"
    },
    "end_date": {
      "type": "string",
      "description": "Optional query parameter. Inclusive end date YYYY-MM-DD. Defaults to today when start_date is supplied.",
      "examples": [
        "2026-07-19"
      ],
      "title": "End Date"
    },
    "include_components": {
      "type": "boolean",
      "description": "Optional query parameter. Include component scores and source observations.",
      "default": false,
      "title": "Include Components"
    },
    "include_sources": {
      "type": "boolean",
      "description": "Optional query parameter. Include FXMacroData source endpoint URLs.",
      "default": false,
      "title": "Include Sources"
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
    }
  },
  "required": [
    "currency",
    "factor"
  ],
  "additionalProperties": false
}
```
