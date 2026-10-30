### fxmd_mcp_calendar_event_versions

Return immutable schedule and importance versions for a stable archive event ID, including explicit publisher cancellations and source capture evidence. Capture, acceptance and documentary publisher clocks remain distinct. Checkpoint and cursor pin subsequent history pages. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "currency": {
      "description": "3-letter ISO currency code, case-insensitive.",
      "examples": [
        "usd",
        "eur",
        "gbp",
        "jpy"
      ],
      "type": "string"
    },
    "archive_event_id": {
      "description": "Stable archive event_id returned in historical schedule evidence.",
      "maxLength": 200,
      "minLength": 1,
      "pattern": "^[A-Za-z0-9_-]+$",
      "type": "string"
    },
    "checkpoint": {
      "anyOf": [
        {
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Checkpoint returned by the first page."
    },
    "cursor": {
      "anyOf": [
        {
          "maxLength": 2048,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Opaque next_cursor returned by the previous page."
    },
    "limit": {
      "default": 250,
      "description": "Maximum schedule transitions per page, default 250.",
      "maximum": 1000,
      "minimum": 1,
      "type": "integer"
    }
  },
  "required": [
    "currency",
    "archive_event_id"
  ],
  "type": "object",
  "title": "calendar_event_versionsArguments"
}
```
