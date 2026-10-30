### fxmd_announcement_changes

Poll recent live announcement release changes

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "type": "object",
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
      "description": "Optional query parameter. Comma-separated currency codes, `g10`, or `all`. Without a paid API key the result is restricted to USD.",
      "examples": [
        "g10"
      ],
      "title": "Currencies"
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
      "description": "Optional query parameter. Optional comma-separated announcement indicator slugs. Allowed values: afe_dollar_index, average_hourly_earnings, average_hourly_earnings_mom, balance_on_goods, balance_on_services, bank_lending_standards, bgcr, breakeven_inflation_rate, broad_dollar_index, broad_money, building_approvals, building_permits, business_confidence, business_inventories, capital_account_balance, cb_assets, commodity_price_energy, commodity_price_ex_energy, commodity_price_index, commodity_prices, construction_spending, consumer_confidence, core_inflation, core_inflation_median, core_inflation_mom, core_inflation_trim, core_pce, core_pce_mom, credit_growth, crude_oil_inventories, current_account_balance, dairy_exports, deposit_rates, distillate_inventories, durable_goods_orders, effr, eme_dollar_index, employment, employment_cost_index, exports, factory_orders, financial_account_balance, foreign_reserves, full_time_employment, fx_reserves, gasoline_inventories, gdp, gdp_growth_q4_yoy, gold_reserves, gov_bond_10y, gov_bond_15y, gov_bond_1_5m, gov_bond_1m, gov_bond_1y, gov_bond_20y, gov_bond_25y, gov_bond_2m, gov_bond_2y, gov_bond_30y, gov_bond_3m, gov_bond_3y, gov_bond_40y, gov_bond_4m, gov_bond_4y, gov_bond_5y, gov_bond_6m, gov_bond_6y, gov_bond_7y, gov_bond_8y, gov_bond_9y, government_debt, house_price_index, house_prices, household_credit, household_spending, housing_starts, import_prices, imports, industrial_production, inflation, inflation_linked_bond, inflation_mom, initial_jobless_claims, international_assets, international_liabilities, job_openings, m1, m2, m3, nairu, natural_gas_storage, net_foreign_asset_position, non_farm_payrolls, non_farm_payrolls_change, obfr, part_time_employment, participation_rate, pce, pce_mom, policy_rate, policy_rate_midpoint, policy_rate_mlf, policy_rate_mro, policy_rate_target_lower, ppi, primary_income_balance, productivity, real_yield_20y, real_yield_30y, real_yield_5y, real_yield_7y, retail_sales, retail_sales_control_group, retail_sales_ex_autos, retail_sales_ex_autos_and_gas, risk_free_rate, secondary_income_balance, sight_deposits, snb_balance_sheet, sofr_average_180d, sofr_average_30d, sofr_average_90d, sofr_index, terms_of_trade, tgcr, trade_balance, trade_weighted_index, trimmed_mean_inflation, unemployment, wage_price_index, wages, wholesale_inventories.",
      "examples": [
        "inflation,unemployment"
      ],
      "title": "Indicators",
      "enum": [
        "afe_dollar_index",
        "average_hourly_earnings",
        "average_hourly_earnings_mom",
        "balance_on_goods",
        "balance_on_services",
        "bank_lending_standards",
        "bgcr",
        "breakeven_inflation_rate",
        "broad_dollar_index",
        "broad_money",
        "building_approvals",
        "building_permits",
        "business_confidence",
        "business_inventories",
        "capital_account_balance",
        "cb_assets",
        "commodity_price_energy",
        "commodity_price_ex_energy",
        "commodity_price_index",
        "commodity_prices",
        "construction_spending",
        "consumer_confidence",
        "core_inflation",
        "core_inflation_median",
        "core_inflation_mom",
        "core_inflation_trim",
        "core_pce",
        "core_pce_mom",
        "credit_growth",
        "crude_oil_inventories",
        "current_account_balance",
        "dairy_exports",
        "deposit_rates",
        "distillate_inventories",
        "durable_goods_orders",
        "effr",
        "eme_dollar_index",
        "employment",
        "employment_cost_index",
        "exports",
        "factory_orders",
        "financial_account_balance",
        "foreign_reserves",
        "full_time_employment",
        "fx_reserves",
        "gasoline_inventories",
        "gdp",
        "gdp_growth_q4_yoy",
        "gold_reserves",
        "gov_bond_10y",
        "gov_bond_15y",
        "gov_bond_1_5m",
        "gov_bond_1m",
        "gov_bond_1y",
        "gov_bond_20y",
        "gov_bond_25y",
        "gov_bond_2m",
        "gov_bond_2y",
        "gov_bond_30y",
        "gov_bond_3m",
        "gov_bond_3y",
        "gov_bond_40y",
        "gov_bond_4m",
        "gov_bond_4y",
        "gov_bond_5y",
        "gov_bond_6m",
        "gov_bond_6y",
        "gov_bond_7y",
        "gov_bond_8y",
        "gov_bond_9y",
        "government_debt",
        "house_price_index",
        "house_prices",
        "household_credit",
        "household_spending",
        "housing_starts",
        "import_prices",
        "imports",
        "industrial_production",
        "inflation",
        "inflation_linked_bond",
        "inflation_mom",
        "initial_jobless_claims",
        "international_assets",
        "international_liabilities",
        "job_openings",
        "m1",
        "m2",
        "m3",
        "nairu",
        "natural_gas_storage",
        "net_foreign_asset_position",
        "non_farm_payrolls",
        "non_farm_payrolls_change",
        "obfr",
        "part_time_employment",
        "participation_rate",
        "pce",
        "pce_mom",
        "policy_rate",
        "policy_rate_midpoint",
        "policy_rate_mlf",
        "policy_rate_mro",
        "policy_rate_target_lower",
        "ppi",
        "primary_income_balance",
        "productivity",
        "real_yield_20y",
        "real_yield_30y",
        "real_yield_5y",
        "real_yield_7y",
        "retail_sales",
        "retail_sales_control_group",
        "retail_sales_ex_autos",
        "retail_sales_ex_autos_and_gas",
        "risk_free_rate",
        "secondary_income_balance",
        "sight_deposits",
        "snb_balance_sheet",
        "sofr_average_180d",
        "sofr_average_30d",
        "sofr_average_90d",
        "sofr_index",
        "terms_of_trade",
        "tgcr",
        "trade_balance",
        "trade_weighted_index",
        "trimmed_mean_inflation",
        "unemployment",
        "wage_price_index",
        "wages",
        "wholesale_inventories"
      ],
      "example": "afe_dollar_index"
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
      "description": "Optional query parameter. Cursor returned as `next_cursor` by the previous response. ISO 8601 timestamps and Unix epoch seconds are also accepted.",
      "title": "Since"
    },
    "limit": {
      "type": "integer",
      "maximum": 500,
      "minimum": 1,
      "description": "Optional query parameter. Maximum number of matching change events to return.",
      "default": 100,
      "title": "Limit"
    },
    "payload": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Use `compact` for trigger payloads or `full` for row fields. Allowed values: compact, full.",
      "default": "compact",
      "title": "Payload",
      "enum": [
        "compact",
        "full"
      ],
      "example": "compact"
    }
  },
  "required": [],
  "additionalProperties": false
}
```
