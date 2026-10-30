### fxmd_positioning_history

CFTC contract positioning history

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "type": "object",
  "properties": {
    "instrument": {
      "type": "string",
      "title": "Instrument",
      "description": "Required path parameter."
    },
    "report": {
      "type": "string",
      "default": "legacy_futures",
      "title": "Report",
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
    "limit": {
      "type": "integer",
      "maximum": 5000,
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
    "instrument"
  ],
  "additionalProperties": false
}
```
