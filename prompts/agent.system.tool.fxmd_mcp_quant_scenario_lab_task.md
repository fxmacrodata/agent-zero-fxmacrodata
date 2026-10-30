### fxmd_mcp_quant_scenario_lab_task

Run an expanded quant-style policy scenario for an FX pair with deterministic projection, stress percentiles, and horizon assumptions. Returns analysis in the tool response. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "base": {
      "description": "Base currency, 3-letter ISO code (case-insensitive). Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "eur",
        "gbp",
        "aud",
        "usd"
      ],
      "type": "string"
    },
    "quote": {
      "description": "Quote currency, 3-letter ISO code (case-insensitive). Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "usd",
        "jpy",
        "chf"
      ],
      "type": "string"
    },
    "shock_leg": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "base",
      "description": "Which leg receives the policy shock: base or quote.",
      "examples": [
        "base",
        "quote"
      ]
    },
    "shock_bps": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": 50.0,
      "description": "Policy shock size in basis points (100 bps = 1.00 percentage point).",
      "examples": [
        25.0,
        50.0,
        -25.0
      ]
    },
    "elasticity_per_100bps": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": 0.8,
      "description": "Heuristic percent FX move per 100 bps spread change.",
      "examples": [
        0.5,
        0.8,
        1.2
      ]
    },
    "annualized_volatility_pct": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": 8.0,
      "description": "Annualized volatility assumption (percent) for stress-band construction.",
      "examples": [
        6.0,
        8.0,
        12.0
      ]
    },
    "horizon_days": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 30,
      "description": "Scenario horizon in calendar days.",
      "examples": [
        7,
        30,
        90
      ]
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
      "description": "Optional inclusive lower bound, YYYY-MM-DD.",
      "examples": [
        "2020-01-01",
        "2024-06-30"
      ]
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
      "description": "Optional inclusive upper bound, YYYY-MM-DD.",
      "examples": [
        "2020-01-01",
        "2024-06-30"
      ]
    }
  },
  "required": [
    "base",
    "quote"
  ],
  "type": "object",
  "title": "quant_scenario_lab_taskArguments"
}
```
