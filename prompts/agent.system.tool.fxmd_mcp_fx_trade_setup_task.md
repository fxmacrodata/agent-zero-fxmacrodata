### fxmd_mcp_fx_trade_setup_task

Build a trader-oriented FX pair setup using spot context, macro differentials, upcoming catalyst risk, and optional COT positioning. Returns analysis in the tool response. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "base": {
      "description": "Base currency, 3-letter ISO code. Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "eur",
        "gbp",
        "aud"
      ],
      "type": "string"
    },
    "quote": {
      "description": "Quote currency, 3-letter ISO code. Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "usd",
        "jpy",
        "chf"
      ],
      "type": "string"
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
      "description": "Maximum upcoming catalysts per leg to rank.",
      "examples": [
        3,
        4,
        6
      ]
    },
    "include_cot": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "When true, attempt to include COT positioning context for both legs.",
      "examples": [
        true,
        false
      ]
    }
  },
  "required": [
    "base",
    "quote"
  ],
  "type": "object",
  "title": "fx_trade_setup_taskArguments"
}
```
