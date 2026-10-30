### fxmd_native_history

Reserves, Treasury and energy history

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "type": "object",
  "properties": {
    "source": {
      "type": "string",
      "title": "Source",
      "description": "Required path parameter."
    },
    "year": {
      "type": "integer",
      "maximum": 2100,
      "minimum": 1900,
      "title": "Year",
      "description": "Required query parameter."
    },
    "measure": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 100
        },
        {
          "type": "null"
        }
      ],
      "title": "Measure",
      "description": "Optional query parameter."
    },
    "holder_country_code": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 30
        },
        {
          "type": "null"
        }
      ],
      "title": "Holder Country Code",
      "description": "Optional query parameter."
    },
    "ownership_basis": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 100
        },
        {
          "type": "null"
        }
      ],
      "title": "Ownership Basis",
      "description": "Optional query parameter."
    },
    "maturity": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 60
        },
        {
          "type": "null"
        }
      ],
      "title": "Maturity",
      "description": "Optional query parameter."
    },
    "account_type": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 160
        },
        {
          "type": "null"
        }
      ],
      "title": "Account Type",
      "description": "Optional query parameter."
    },
    "region": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 160
        },
        {
          "type": "null"
        }
      ],
      "title": "Region",
      "description": "Optional query parameter."
    },
    "product": {
      "anyOf": [
        {
          "type": "string",
          "maxLength": 160
        },
        {
          "type": "null"
        }
      ],
      "title": "Product",
      "description": "Optional query parameter."
    },
    "limit": {
      "type": "integer",
      "maximum": 5000,
      "minimum": 1,
      "default": 100,
      "title": "Limit",
      "description": "Optional query parameter."
    },
    "offset": {
      "type": "integer",
      "minimum": 0,
      "default": 0,
      "title": "Offset",
      "description": "Optional query parameter."
    },
    "order": {
      "type": "string",
      "pattern": "^(asc|desc)$",
      "default": "asc",
      "title": "Order",
      "description": "Optional query parameter."
    }
  },
  "required": [
    "source",
    "year"
  ],
  "additionalProperties": false
}
```
