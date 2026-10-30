### fxmd_financial_prices

Official financial prices and yield curves

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "type": "object",
  "properties": {
    "currency": {
      "type": "string",
      "title": "Currency",
      "description": "Required path parameter."
    },
    "source": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 80
        },
        {
          "type": "null"
        }
      ],
      "title": "Source",
      "description": "Optional query parameter."
    },
    "start_date": {
      "anyOf": [
        {
          "type": "string",
          "format": "date"
        },
        {
          "type": "null"
        }
      ],
      "title": "Start Date",
      "description": "Optional query parameter."
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string",
          "format": "date"
        },
        {
          "type": "null"
        }
      ],
      "title": "End Date",
      "description": "Optional query parameter."
    },
    "measure": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 60
        },
        {
          "type": "null"
        }
      ],
      "title": "Measure",
      "description": "Optional query parameter."
    },
    "instrument_id": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 240
        },
        {
          "type": "null"
        }
      ],
      "title": "Instrument Id",
      "description": "Optional query parameter."
    },
    "issuer": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 240
        },
        {
          "type": "null"
        }
      ],
      "title": "Issuer",
      "description": "Optional query parameter."
    },
    "limit": {
      "type": "integer",
      "maximum": 100,
      "minimum": 1,
      "default": 100,
      "title": "Limit",
      "description": "Optional query parameter."
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "default": 0,
      "title": "Offset",
      "description": "Optional query parameter."
    }
  },
  "required": [
    "currency"
  ],
  "additionalProperties": false
}
```
