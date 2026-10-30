### fxmd_mcp_official_dataset_family

Get metadata-first official dataset payloads grouped by API endpoint type. `endpoint_type` selects the API taxonomy group and `dataset` selects the specific series family. Supported endpoint types: monetary_policy, fiscal_policy, international_trade, statistics_releases. Supported datasets: auction_metrics, bop, capital_flows, cb_liquidity, credit_conditions, external_debt, fx_intervention, iip, services_trade, treasury_cash, wage_settlements. Access: requires an FXMacroData API key; an anonymous call returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "endpoint_type": {
      "description": "Endpoint taxonomy group from the API structure. Supported: monetary_policy, fiscal_policy, international_trade, statistics_releases.",
      "examples": [
        "monetary_policy",
        "fiscal_policy",
        "international_trade",
        "statistics_releases"
      ],
      "type": "string"
    },
    "dataset": {
      "description": "Dataset slug within the selected endpoint_type. Supported: auction_metrics, bop, capital_flows, cb_liquidity, credit_conditions, external_debt, fx_intervention, iip, services_trade, treasury_cash, wage_settlements.",
      "examples": [
        "cb_liquidity",
        "treasury_cash",
        "bop",
        "credit_conditions"
      ],
      "type": "string"
    },
    "currency": {
      "description": "3-letter ISO currency code (case-insensitive).",
      "examples": [
        "usd",
        "eur",
        "gbp",
        "jpy"
      ],
      "type": "string"
    },
    "component": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Required only when dataset='bop'. Supported bop components: goods_balance, services_balance, primary_income, secondary_income, current_account, capital_account, financial_account.",
      "examples": [
        "current_account",
        "services_balance",
        "financial_account"
      ]
    }
  },
  "required": [
    "endpoint_type",
    "dataset",
    "currency"
  ],
  "type": "object",
  "title": "official_dataset_familyArguments"
}
```
