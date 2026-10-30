### fxmd_event_predictions

List predictions for one indicator of a currency

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
      "description": "Required path parameter. Allowed values: AUD, BRL, CAD, CHF, CNH, CNY, DKK, EUR, GBP, HUF, ILS, JPY, KRW, MYR, NGN, NOK, NZD, PEN, SEK, THB, TWD, USD."
    },
    "indicator": {
      "type": "string",
      "description": "Required path parameter. Indicator slug Allowed values: afe_dollar_index, average_hourly_earnings, average_hourly_earnings_mom, balance_on_goods, balance_on_services, bank_lending_standards, bgcr, breakeven_inflation_rate, broad_dollar_index, broad_money, building_approvals, building_permits, business_confidence, business_inventories, capital_account_balance, cb_assets, commodity_price_energy, commodity_price_ex_energy, commodity_price_index, commodity_prices, construction_spending, consumer_confidence, core_inflation, core_inflation_median, core_inflation_mom, core_inflation_trim, core_pce, core_pce_mom, credit_growth, crude_oil_inventories, current_account_balance, dairy_exports, deposit_rates, distillate_inventories, durable_goods_orders, effr, eme_dollar_index, employment, employment_cost_index, exports, factory_orders, financial_account_balance, foreign_reserves, full_time_employment, fx_reserves, gasoline_inventories, gdp, gdp_growth_q4_yoy, gold_reserves, gov_bond_10y, gov_bond_15y, gov_bond_1_5m, gov_bond_1m, gov_bond_1y, gov_bond_20y, gov_bond_25y, gov_bond_2m, gov_bond_2y, gov_bond_30y, gov_bond_3m, gov_bond_3y, gov_bond_40y, gov_bond_4m, gov_bond_4y, gov_bond_5y, gov_bond_6m, gov_bond_6y, gov_bond_7y, gov_bond_8y, gov_bond_9y, government_debt, house_price_index, house_prices, household_credit, household_spending, housing_starts, import_prices, imports, industrial_production, inflation, inflation_linked_bond, inflation_mom, initial_jobless_claims, international_assets, international_liabilities, job_openings, m1, m2, m3, nairu, natural_gas_storage, net_foreign_asset_position, non_farm_payrolls, non_farm_payrolls_change, obfr, part_time_employment, participation_rate, pce, pce_mom, policy_rate, policy_rate_midpoint, policy_rate_mlf, policy_rate_mro, policy_rate_target_lower, ppi, primary_income_balance, productivity, real_yield_20y, real_yield_30y, real_yield_5y, real_yield_7y, retail_sales, retail_sales_control_group, retail_sales_ex_autos, retail_sales_ex_autos_and_gas, risk_free_rate, secondary_income_balance, sight_deposits, snb_balance_sheet, sofr_average_180d, sofr_average_30d, sofr_average_90d, sofr_index, terms_of_trade, tgcr, trade_balance, trade_weighted_index, trimmed_mean_inflation, unemployment, wage_price_index, wages, wholesale_inventories.",
      "examples": [
        "inflation"
      ],
      "title": "Indicator",
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
      "description": "Optional query parameter. Filter by how the forecast was produced. Prefer this over `prediction_type`: one class can span several legacy types, which is how `forecaster_survey` returns both the ECB and Philadelphia Fed Surveys of Professional Forecasters.",
      "title": "Prediction Class"
    },
    "prediction_type": {
      "anyOf": [
        {
          "enum": [
            "market_consensus",
            "market_prediction",
            "model_nowcast",
            "survey",
            "central_bank_forecast",
            "central_bank_projection",
            "imf_weo",
            "oecd_eo",
            "fxmacrodata"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Optional legacy prediction-type filter, retained unchanged for existing clients. Superseded by `prediction_class`.",
      "title": "Prediction Type"
    },
    "prediction_source": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Optional source identifier filter.",
      "title": "Prediction Source"
    },
    "official_limit": {
      "type": "integer",
      "maximum": 2000,
      "minimum": 0,
      "description": "Optional query parameter. Maximum rows in ``official_forecasts`` (native-period official forecasts and surveys). 0 omits them.",
      "default": 500,
      "title": "Official Limit"
    },
    "pre_release_only": {
      "type": "boolean",
      "description": "Optional query parameter. Return only forecasts with `generated_at` strictly before the linked `announcement_datetime` (default: true). FXMacroData only publishes forecasts generated before the announcement, so this flag is informational: setting it to false does not return additional rows.",
      "default": true,
      "title": "Pre Release Only"
    },
    "seasonality": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Optional seasonal adjustment selector, matching /v1/announcements. Allowed values: sa, nsa.",
      "title": "Seasonality",
      "enum": [
        "sa",
        "nsa"
      ],
      "example": "sa"
    },
    "frequency": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Optional returned change basis selector, matching /v1/announcements. Allowed values: level, yoy, qoq, mom.",
      "title": "Frequency",
      "enum": [
        "level",
        "yoy",
        "qoq",
        "mom"
      ],
      "example": "level"
    },
    "annualization": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Optional annualization selector, matching /v1/announcements. Allowed values: not_annualized, saar.",
      "title": "Annualization",
      "enum": [
        "not_annualized",
        "saar"
      ],
      "example": "not_annualized"
    },
    "period_aggregation": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Optional period aggregation selector, matching /v1/announcements. Allowed values: monthly, quarterly, annual, quarterly_average, annual_average.",
      "title": "Period Aggregation",
      "enum": [
        "monthly",
        "quarterly",
        "annual",
        "quarterly_average",
        "annual_average"
      ],
      "example": "monthly"
    },
    "basis": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Optional real/nominal selector, matching /v1/announcements. Allowed values: real, nominal.",
      "title": "Basis",
      "enum": [
        "real",
        "nominal"
      ],
      "example": "real"
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
      "description": "Optional query parameter. Start date YYYY-MM-DD (period date). Defaults to 180 days before today when omitted.",
      "title": "Start Date"
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
      "description": "Optional query parameter. End date YYYY-MM-DD (period date). Defaults to 90 days ahead when omitted.",
      "title": "End Date"
    },
    "limit": {
      "type": "integer",
      "maximum": 100,
      "minimum": 1,
      "description": "Optional query parameter. Maximum number of prediction groups to return in `data[]`. Use with `offset` to page through long histories. Defaults to 20. Maximum 100.",
      "examples": [
        20
      ],
      "default": 20,
      "title": "Limit"
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Optional query parameter. Number of prediction groups to skip from the start of `data[]`. Use with `limit` for pagination. Defaults to 0.",
      "examples": [
        0
      ],
      "default": 0,
      "title": "Offset"
    },
    "page": {
      "anyOf": [
        {
          "type": "integer",
          "minimum": 1
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. One-based page number. When supplied, it takes precedence over offset.",
      "examples": [
        1
      ],
      "title": "Page"
    },
    "before_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Return groups strictly before this YYYY-MM-DD period date. Use the previous response's `next_cursor` for bounded pagination.",
      "title": "Before Date"
    },
    "as_of": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "As Of",
      "description": "Optional query parameter."
    },
    "event_compatible_only": {
      "type": "boolean",
      "default": false,
      "title": "Event Compatible Only",
      "description": "Optional query parameter."
    }
  },
  "required": [
    "currency",
    "indicator"
  ],
  "additionalProperties": false
}
```
