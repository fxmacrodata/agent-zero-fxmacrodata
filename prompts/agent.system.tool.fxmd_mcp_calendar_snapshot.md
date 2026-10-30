### fxmd_mcp_calendar_snapshot

Return persisted economic-event schedules, importance and cancellation states at an explicit historical cutoff. Accepted mode requires actual capture and parser acceptance by the cutoff. Reconstruction additionally admits qualified official notices recovered later; it does not establish historical service availability. Scheduled-date and event filters apply after version selection. Checkpoint and cursor pin subsequent export pages. Empty results do not establish that no events were scheduled. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

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
    "as_of": {
      "description": "Required ISO 8601 knowledge cutoff with UTC offset or Z.",
      "examples": [
        "2025-10-01T15:00:00Z"
      ],
      "format": "date-time",
      "pattern": ".*(?:Z|[+-]\\d{2}:\\d{2})$",
      "type": "string"
    },
    "knowledge_mode": {
      "default": "accepted",
      "description": "Archive acceptance replay, or qualified documentary reconstruction.",
      "enum": [
        "accepted",
        "reconstruction"
      ],
      "type": "string"
    },
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Inclusive scheduled-date lower bound, YYYY-MM-DD."
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Inclusive scheduled-date upper bound, YYYY-MM-DD."
    },
    "importance": {
      "anyOf": [
        {
          "enum": [
            "high",
            "medium",
            "low",
            "unknown"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Frozen event importance filter."
    },
    "event_kind": {
      "anyOf": [
        {
          "enum": [
            "release",
            "speech",
            "meeting",
            "policy_decision",
            "press_conference",
            "other"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Scheduled event kind filter."
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
      "description": "Maximum events per page, default 250.",
      "maximum": 1000,
      "minimum": 1,
      "type": "integer"
    }
  },
  "required": [
    "currency",
    "as_of"
  ],
  "type": "object",
  "title": "calendar_snapshotArguments"
}
```
