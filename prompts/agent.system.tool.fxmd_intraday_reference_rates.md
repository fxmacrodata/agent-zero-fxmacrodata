### fxmd_intraday_reference_rates

Get subscriber intraday FX reference rates

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
    "start_time": {
      "anyOf": [
        {
          "type": "string",
          "format": "date-time"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Inclusive RFC 3339 timestamp. Defaults to 24 hours before end_time.",
      "examples": [
        "2026-07-13T00:00:00Z"
      ],
      "title": "Start Time"
    },
    "end_time": {
      "anyOf": [
        {
          "type": "string",
          "format": "date-time"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Inclusive RFC 3339 source timestamp. Defaults to the current time.",
      "examples": [
        "2026-07-14T00:00:00Z"
      ],
      "title": "End Time"
    }
  },
  "required": [
    "base",
    "quote"
  ],
  "additionalProperties": false
}
```
