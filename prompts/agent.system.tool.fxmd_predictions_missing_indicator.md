### fxmd_predictions_missing_indicator

Page official forecast vintages from one publisher

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
    "prediction_source": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 160
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Required publisher identifier for source-scoped native forecast history.",
      "title": "Prediction Source"
    },
    "prediction_class": {
      "anyOf": [
        {
          "enum": [
            "compiled_consensus",
            "forecaster_survey",
            "expectations_survey",
            "market_implied",
            "model_nowcast",
            "central_bank_projection",
            "institutional_projection",
            "fxmacrodata"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Prediction Class",
      "description": "Optional query parameter."
    },
    "statistic": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 80
        },
        {
          "type": "null"
        }
      ],
      "title": "Statistic",
      "description": "Optional query parameter."
    },
    "respondent_population": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 120
        },
        {
          "type": "null"
        }
      ],
      "title": "Respondent Population",
      "description": "Optional query parameter."
    },
    "start_date": {
      "anyOf": [
        {
          "type": "string",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
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
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        },
        {
          "type": "null"
        }
      ],
      "title": "End Date",
      "description": "Optional query parameter."
    },
    "variable": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 250
        },
        {
          "type": "null"
        }
      ],
      "title": "Variable",
      "description": "Optional query parameter."
    },
    "target_period": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 160
        },
        {
          "type": "null"
        }
      ],
      "title": "Target Period",
      "description": "Optional query parameter."
    },
    "publication_precision": {
      "anyOf": [
        {
          "enum": [
            "exact",
            "date",
            "unknown"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Publication Precision",
      "description": "Optional query parameter."
    },
    "before_id": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 256
        },
        {
          "type": "null"
        }
      ],
      "title": "Before Id",
      "description": "Optional query parameter."
    },
    "limit": {
      "type": "integer",
      "maximum": 1000,
      "minimum": 1,
      "default": 100,
      "title": "Limit",
      "description": "Optional query parameter."
    }
  },
  "required": [
    "currency"
  ],
  "additionalProperties": false
}
```
