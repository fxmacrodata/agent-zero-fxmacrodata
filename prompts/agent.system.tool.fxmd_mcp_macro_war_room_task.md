### fxmd_mcp_macro_war_room_task

Build a multi-panel macro market cockpit that combines FX sessions, upcoming release queue, pair context, and generated risk alerts. Returns analysis in the tool response. Access: USD is available without an API key; every other currency returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "base": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Base currency for pair context, 3-letter ISO code (case-insensitive). Defaults to the release currency when omitted. Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "eur",
        "gbp",
        "aud",
        "usd"
      ]
    },
    "quote": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "usd",
      "description": "Quote currency for pair context, 3-letter ISO code (case-insensitive). Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "usd",
        "jpy",
        "chf"
      ]
    },
    "currency": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "usd",
      "description": "Release currency used for queue and spotlight indicator. Supported: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD.",
      "examples": [
        "usd",
        "eur",
        "gbp"
      ]
    },
    "indicator": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "inflation",
      "description": "Spotlight indicator slug for release context. Supported examples: afe_dollar_index, average_hourly_earnings, average_hourly_earnings_mom, balance_on_goods, balance_on_services, bank_lending_standards, bgcr, breakeven_inflation_rate, broad_dollar_index, broad_money, building_approvals, building_permits, business_confidence, business_inventories, capital_account_balance, cb_assets, commodity_price_energy, commodity_price_ex_energy, commodity_price_index, commodity_prices, construction_spending, consumer_confidence, core_inflation, core_inflation_median, core_inflation_mom, core_inflation_trim, core_pce, core_pce_mom, credit_growth, crude_oil_inventories, current_account_balance, dairy_exports, deposit_rates, distillate_inventories, durable_goods_orders, effr, eme_dollar_index, employment, employment_cost_index, exports, factory_orders, financial_account_balance, foreign_reserves, full_time_employment, fx_reserves, gasoline_inventories, gdp, gdp_growth_q4_yoy, gold_reserves, gov_bond_10y, gov_bond_15y, gov_bond_1_5m, gov_bond_1m, gov_bond_1y, gov_bond_20y, gov_bond_25y, gov_bond_2m, gov_bond_2y, gov_bond_30y, gov_bond_3m, gov_bond_3y, gov_bond_40y, gov_bond_4m, gov_bond_4y, gov_bond_5y, gov_bond_6m, gov_bond_6y, gov_bond_7y, gov_bond_8y, gov_bond_9y, government_debt, house_price_index, house_prices, household_credit, household_spending, housing_starts, import_prices, imports, industrial_production, inflation, inflation_linked_bond, inflation_mom, initial_jobless_claims, international_assets, international_liabilities, job_openings, m1, m2, m3, nairu, natural_gas_storage, net_foreign_asset_position, non_farm_payrolls, non_farm_payrolls_change, obfr, part_time_employment, participation_rate, pce, pce_mom, policy_rate, policy_rate_midpoint, policy_rate_mlf, policy_rate_mro, policy_rate_target_lower, ppi, primary_income_balance, productivity, real_yield_20y, real_yield_30y, real_yield_5y, real_yield_7y, retail_sales, retail_sales_control_group, retail_sales_ex_autos, retail_sales_ex_autos_and_gas, risk_free_rate, secondary_income_balance, sight_deposits, snb_balance_sheet, sofr_average_180d, sofr_average_30d, sofr_average_90d, sofr_index, terms_of_trade, tgcr, trade_balance, trade_weighted_index, trimmed_mean_inflation, unemployment, wage_price_index, wages, wholesale_inventories.",
      "examples": [
        "inflation",
        "policy_rate",
        "gdp"
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
  "type": "object",
  "title": "macro_war_room_taskArguments"
}
```
