### fxmd_risk_sentiment

Global risk-on / risk-off indicator

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "type": "object",
  "properties": {
    "start_date": {
      "type": "string",
      "description": "Optional query parameter. Start date YYYY-MM-DD",
      "examples": [
        "2025-12-01"
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
  "required": [],
  "additionalProperties": false
}
```
