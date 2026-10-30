### fxmd_calendar_snapshot

Get the economic schedule known at a historical time

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
        "BRL",
        "CAD",
        "CHF",
        "CNH",
        "CNY",
        "COMM",
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
      "example": "AUD",
      "description": "Required path parameter. Allowed values: AUD, BRL, CAD, CHF, CNH, CNY, COMM, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD."
    },
    "as_of": {
      "type": "string",
      "format": "date-time",
      "description": "Required query parameter. Knowledge cutoff, ISO 8601 with UTC offset.",
      "title": "As Of"
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
      "title": "Importance",
      "description": "Optional query parameter."
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
      "title": "Event Kind",
      "description": "Optional query parameter."
    },
    "knowledge_mode": {
      "enum": [
        "accepted",
        "reconstruction"
      ],
      "type": "string",
      "default": "accepted",
      "title": "Knowledge Mode",
      "description": "Optional query parameter."
    },
    "checkpoint": {
      "anyOf": [
        {
          "type": "integer",
          "minimum": 0
        },
        {
          "type": "null"
        }
      ],
      "title": "Checkpoint",
      "description": "Optional query parameter."
    },
    "cursor": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 2048
        },
        {
          "type": "null"
        }
      ],
      "title": "Cursor",
      "description": "Optional query parameter."
    },
    "limit": {
      "type": "integer",
      "maximum": 1000,
      "minimum": 1,
      "default": 250,
      "title": "Limit",
      "description": "Optional query parameter."
    }
  },
  "required": [
    "currency",
    "as_of"
  ],
  "additionalProperties": false
}
```
