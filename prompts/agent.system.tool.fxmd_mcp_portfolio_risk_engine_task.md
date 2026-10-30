### fxmd_mcp_portfolio_risk_engine_task

Analyze a multi-position FX book for concentration, stress exposure, and event-driven catalyst risk. Returns analysis in the tool response. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "positions_json": {
      "description": "JSON array of FX positions. Each item should include base, quote, side (long/short), and notional. Example: [{\"base\":\"eur\",\"quote\":\"usd\",\"side\":\"long\",\"notional\":100000}]",
      "examples": [
        "[{\"base\":\"eur\",\"quote\":\"usd\",\"side\":\"long\",\"notional\":100000},{\"base\":\"gbp\",\"quote\":\"usd\",\"side\":\"short\",\"notional\":80000}]"
      ],
      "type": "string"
    },
    "stress_shock_pct": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": 1.0,
      "description": "Stress shock in percent applied to each pair.",
      "examples": [
        0.5,
        1.0,
        2.0
      ]
    },
    "horizon_events": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 4,
      "description": "Maximum release events to consider per currency leg.",
      "examples": [
        3,
        4,
        8
      ]
    }
  },
  "required": [
    "positions_json"
  ],
  "type": "object",
  "title": "portfolio_risk_engine_taskArguments"
}
```
