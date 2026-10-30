### fxmd_mcp_announcement_changes

Poll recently ingested macro announcement changes with a resumable cursor. This is the bounded, MCP-safe counterpart to the release-event stream: the returned next_cursor is accepted as `since` on a later call, so polling resumes without holding a streaming invocation open. Access: USD is available without an API key; every other currency returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "currencies": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional comma-separated currency codes, `g10`, or `all`. Without subscriber access, results are limited to the public scope.",
      "examples": [
        "usd,eur",
        "g10"
      ]
    },
    "indicators": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional comma-separated announcement indicator slugs.",
      "examples": [
        "inflation,policy_rate"
      ]
    },
    "since": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional previous next_cursor, ISO 8601 timestamp, or Unix epoch seconds.",
      "examples": [
        "2026-07-21T00:00:00Z"
      ]
    },
    "limit": {
      "default": 100,
      "description": "Maximum matching change events to return.",
      "examples": [
        50,
        100
      ],
      "maximum": 500,
      "minimum": 1,
      "type": "integer"
    },
    "payload": {
      "default": "compact",
      "description": "Event payload shape: compact trigger rows or full announcement rows.",
      "examples": [
        "compact",
        "full"
      ],
      "type": "string"
    }
  },
  "type": "object",
  "title": "announcement_changesArguments"
}
```
