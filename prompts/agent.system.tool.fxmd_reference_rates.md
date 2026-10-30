### fxmd_reference_rates

Get timestamped official FX reference rates

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "type": "object",
  "properties": {
    "base": {
      "type": "string",
      "description": "Required path parameter. Base currency code",
      "examples": [
        "EUR"
      ],
      "title": "Base"
    },
    "quote": {
      "type": "string",
      "description": "Required path parameter. Quote currency code",
      "examples": [
        "USD"
      ],
      "title": "Quote"
    },
    "date": {
      "type": "string",
      "description": "Optional query parameter. Single reference date YYYY-MM-DD. Overrides start_date/end_date.",
      "examples": [
        "2026-07-10"
      ],
      "title": "Date"
    },
    "start_date": {
      "type": "string",
      "description": "Optional query parameter. Start reference date YYYY-MM-DD, inclusive. Without end_date the window runs through the latest available date (today, UTC); page through long histories with limit and offset or page.",
      "examples": [
        "2026-07-10"
      ],
      "title": "Start Date"
    },
    "end_date": {
      "type": "string",
      "description": "Optional query parameter. End reference date YYYY-MM-DD, inclusive. Without start_date only this date is returned. With neither start_date nor end_date, today's (UTC) reference date is returned.",
      "examples": [
        "2026-07-10"
      ],
      "title": "End Date"
    },
    "source": {
      "type": "string",
      "description": "Optional query parameter. Optional source id filter, for example ecb_eurofxref_daily.",
      "title": "Source"
    },
    "timestamp_type": {
      "type": "string",
      "description": "Optional query parameter. Optional timestamp type filter, for example fixing or published.",
      "title": "Timestamp Type"
    },
    "native_only": {
      "type": "boolean",
      "description": "Optional query parameter. Return only rows published directly for the requested pair, excluding inverse and cross-derived rows.",
      "default": false,
      "title": "Native Only"
    },
    "include_source_legs": {
      "type": "boolean",
      "description": "Optional query parameter. Include derivation source legs when a rate is inverted or crossed.",
      "default": true,
      "title": "Include Source Legs"
    },
    "order": {
      "enum": [
        "timestamp_asc",
        "timestamp_desc",
        "date_asc",
        "date_desc"
      ],
      "type": "string",
      "description": "Optional query parameter. Result ordering.",
      "default": "timestamp_asc",
      "title": "Order"
    },
    "limit": {
      "type": "integer",
      "maximum": 100,
      "minimum": 1,
      "description": "Optional query parameter. Maximum rows to return. Maximum 100.",
      "default": 100,
      "title": "Limit"
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Optional query parameter. Number of rows to skip.",
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
      "description": "Optional query parameter. One-based page number.",
      "title": "Page"
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
      "description": "Optional query parameter. Pin first-page content version; changed history returns 409.",
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
