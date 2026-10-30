### fxmd_indicator_history

Get macroeconomic indicator data

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
      "example": "afe_dollar_index",
      "description": "Required path parameter. Allowed values: afe_dollar_index, average_hourly_earnings, average_hourly_earnings_mom, balance_on_goods, balance_on_services, bank_lending_standards, bgcr, breakeven_inflation_rate, broad_dollar_index, broad_money, building_approvals, building_permits, business_confidence, business_inventories, capital_account_balance, cb_assets, commodity_price_energy, commodity_price_ex_energy, commodity_price_index, commodity_prices, construction_spending, consumer_confidence, core_inflation, core_inflation_median, core_inflation_mom, core_inflation_trim, core_pce, core_pce_mom, credit_growth, crude_oil_inventories, current_account_balance, dairy_exports, deposit_rates, distillate_inventories, durable_goods_orders, effr, eme_dollar_index, employment, employment_cost_index, exports, factory_orders, financial_account_balance, foreign_reserves, full_time_employment, fx_reserves, gasoline_inventories, gdp, gdp_growth_q4_yoy, gold_reserves, gov_bond_10y, gov_bond_15y, gov_bond_1_5m, gov_bond_1m, gov_bond_1y, gov_bond_20y, gov_bond_25y, gov_bond_2m, gov_bond_2y, gov_bond_30y, gov_bond_3m, gov_bond_3y, gov_bond_40y, gov_bond_4m, gov_bond_4y, gov_bond_5y, gov_bond_6m, gov_bond_6y, gov_bond_7y, gov_bond_8y, gov_bond_9y, government_debt, house_price_index, house_prices, household_credit, household_spending, housing_starts, import_prices, imports, industrial_production, inflation, inflation_linked_bond, inflation_mom, initial_jobless_claims, international_assets, international_liabilities, job_openings, m1, m2, m3, nairu, natural_gas_storage, net_foreign_asset_position, non_farm_payrolls, non_farm_payrolls_change, obfr, part_time_employment, participation_rate, pce, pce_mom, policy_rate, policy_rate_midpoint, policy_rate_mlf, policy_rate_mro, policy_rate_target_lower, ppi, primary_income_balance, productivity, real_yield_20y, real_yield_30y, real_yield_5y, real_yield_7y, retail_sales, retail_sales_control_group, retail_sales_ex_autos, retail_sales_ex_autos_and_gas, risk_free_rate, secondary_income_balance, sight_deposits, snb_balance_sheet, sofr_average_180d, sofr_average_30d, sofr_average_90d, sofr_index, terms_of_trade, tgcr, trade_balance, trade_weighted_index, trimmed_mean_inflation, unemployment, wage_price_index, wages, wholesale_inventories."
    },
    "start_date": {
      "type": "string",
      "description": "Optional query parameter. Start date YYYY-MM-DD",
      "examples": [
        "2025-01-01"
      ],
      "title": "Start Date"
    },
    "end_date": {
      "type": "string",
      "description": "Optional query parameter. End date YYYY-MM-DD",
      "examples": [
        "2026-03-01"
      ],
      "title": "End Date"
    },
    "series_mode": {
      "type": "string",
      "pattern": "^(raw|canonical)$",
      "description": "Optional query parameter. Optional series rendering mode. `canonical` applies configured remap rules (for continuity across methodology transitions). `raw` returns the direct indicator series without remapping.",
      "examples": [
        "raw"
      ],
      "default": "raw",
      "title": "Series Mode"
    },
    "limit": {
      "type": "integer",
      "maximum": 100,
      "minimum": 1,
      "description": "Optional query parameter. Maximum number of rows to return in `data[]`. Rows are ordered most-recent-first, so `limit=10` returns the 10 most recent observations within the requested window. Use together with `offset` to page through long histories. Defaults to 20. Maximum 100.",
      "examples": [
        20
      ],
      "default": 20,
      "title": "Limit"
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "description": "Optional query parameter. Number of rows to skip from the start of `data[]` (after most-recent-first ordering). Use with `limit` for pagination. Defaults to 0.",
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
      "description": "Optional query parameter. One-based page number for callers that prefer page-based pagination. When supplied, `offset` is derived as `(page - 1) * limit`.",
      "examples": [
        1
      ],
      "title": "Page"
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
      "description": "Optional query parameter. Optional seasonal adjustment selector. Supported public values are `sa` and `nsa`; check `supported_options.seasonality` in the response/catalogue for values available on this endpoint. Allowed values: sa, nsa.",
      "examples": [
        "sa"
      ],
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
      "description": "Optional query parameter. Optional returned change basis. Supported public values are `level`, `yoy`, `qoq`, and `mom`; check `supported_options.frequency` for values available on this endpoint. Allowed values: level, yoy, qoq, mom.",
      "examples": [
        "yoy"
      ],
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
      "description": "Optional query parameter. Optional annualization selector. Supported public values are `not_annualized` and `saar`; check `supported_options.annualization` for values available on this endpoint. Allowed values: not_annualized, saar.",
      "examples": [
        "saar"
      ],
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
      "description": "Optional query parameter. Optional native-period selector: `monthly`, `quarterly`, `annual`, `quarterly_average`, or `annual_average`. Selects publisher observations without resampling or changing totals into averages; check `supported_options.period_aggregation` for values available on this endpoint. Allowed values: monthly, quarterly, annual, quarterly_average, annual_average.",
      "examples": [
        "quarterly_average"
      ],
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
    "revisions": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Optional revision view. Supported public values are `latest`, `first`, `final`, and `all`; unsupported views return `unsupported_series_option` with supported values. Allowed values: latest, first, final, all.",
      "examples": [
        "latest"
      ],
      "default": "latest",
      "title": "Revisions",
      "enum": [
        "latest",
        "first",
        "final",
        "all"
      ],
      "example": "latest"
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
      "description": "Optional query parameter. Optional real/nominal selector. Supported public values are `real` and `nominal`; only endpoints with known basis metadata accept it. Allowed values: real, nominal.",
      "examples": [
        "real"
      ],
      "title": "Basis",
      "enum": [
        "real",
        "nominal"
      ],
      "example": "real"
    },
    "official_only": {
      "type": "boolean",
      "description": "Optional query parameter. When true, return only official-source rows and remove explicit fallback observations. Prohibited private aggregator rows are always removed regardless of this setting.",
      "examples": [
        true
      ],
      "default": true,
      "title": "Official Only"
    },
    "fields": {
      "anyOf": [
        {
          "type": "string",
          "pattern": "^(full|compact)$"
        },
        {
          "type": "null"
        }
      ],
      "description": "Optional query parameter. Row field set. Omitted or `full` returns every documented row field. `compact` returns only `date`, `val`, `previous_value`, `change_from_previous`, `announcement_datetime`, `announcement_datetime_local` and `publication_time_status` per row, with the revision ledger folded into `revisions_summary` (`count`, `first`, `latest`, `revised`). The envelope, pagination and `dataset_version` are unchanged.",
      "examples": [
        "compact"
      ],
      "title": "Fields"
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
    "availability": {
      "enum": [
        "public",
        "captured"
      ],
      "type": "string",
      "default": "public",
      "title": "Availability",
      "description": "Optional query parameter."
    },
    "dataset_version": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Dataset Version",
      "description": "Optional query parameter."
    },
    "value_mode": {
      "enum": [
        "normalized",
        "source"
      ],
      "type": "string",
      "default": "normalized",
      "title": "Value Mode",
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
