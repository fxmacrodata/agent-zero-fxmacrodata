### fxmd_research_panel

Build a panel of values known at each decision time

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "type": "object",
  "properties": {
    "body": {
      "properties": {
        "series": {
          "items": {
            "properties": {
              "currency": {
                "type": "string",
                "pattern": "^[A-Za-z]{3}$",
                "title": "Currency"
              },
              "indicator": {
                "type": "string",
                "pattern": "^[a-z][a-z0-9_]*$",
                "title": "Indicator"
              },
              "max_age_days": {
                "anyOf": [
                  {
                    "type": "integer",
                    "maximum": 36500.0,
                    "minimum": 0.0
                  },
                  {
                    "type": "null"
                  }
                ],
                "title": "Max Age Days"
              },
              "period_aggregation": {
                "anyOf": [
                  {
                    "type": "string",
                    "enum": [
                      "monthly",
                      "quarterly",
                      "annual",
                      "quarterly_average",
                      "annual_average"
                    ]
                  },
                  {
                    "type": "null"
                  }
                ],
                "title": "Period Aggregation"
              }
            },
            "additionalProperties": false,
            "type": "object",
            "required": [
              "currency",
              "indicator"
            ],
            "title": "ResearchSeries"
          },
          "type": "array",
          "maxItems": 6,
          "minItems": 1,
          "title": "Series"
        },
        "decision_times": {
          "items": {
            "type": "string"
          },
          "type": "array",
          "maxItems": 10000,
          "minItems": 1,
          "title": "Decision Times"
        },
        "start_date": {
          "type": "string",
          "format": "date",
          "title": "Start Date"
        },
        "end_date": {
          "type": "string",
          "format": "date",
          "title": "End Date"
        },
        "availability": {
          "type": "string",
          "enum": [
            "public",
            "captured"
          ],
          "title": "Availability",
          "default": "public"
        },
        "dataset_version": {
          "anyOf": [
            {
              "type": "string",
              "pattern": "^[0-9a-f]{64}$"
            },
            {
              "type": "null"
            }
          ],
          "title": "Dataset Version"
        }
      },
      "additionalProperties": false,
      "type": "object",
      "required": [
        "series",
        "decision_times",
        "start_date",
        "end_date"
      ],
      "title": "ResearchPanelRequest",
      "description": "Research panel request body as JSON; preserves the documented request schema."
    }
  },
  "required": [
    "body"
  ],
  "additionalProperties": false
}
```
