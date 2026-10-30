### fxmd_mcp_source_metadata

Read a complete persisted source definition and original footnotes using the immutable metadata SHA256 from a catalogue or native observation. Returns the reconstructed original JSON object with its types and hash. Requires the associated currency's data access. Access: USD is available without an API key; every other currency returns subscription_required with a subscribe link.

Use only the documented operation schema. Credentials and endpoint overrides are never tool arguments. Discover indicator slugs before requesting history. Preserve units, periods, source links, pagination and access notices. Missing data is unavailable, not zero. Do not treat scheduled, observed publication or ingestion timestamps as interchangeable; missing evidence and latency stay unknown. Preserve structured MCP resource blocks; this plugin does not render MCP Apps. FXMacroData-generated forecasts are labelled and are not market consensus. Public USD evaluation may have a recent access window and delay; additional protected coverage requires the user's subscription. This is a read-only external data request, except any explicitly labelled account/subscription helper which only returns its documented link.

Arguments (exact JSON Schema):
```json
{
  "properties": {
    "currency": {
      "type": "string"
    },
    "sha256": {
      "type": "string"
    }
  },
  "required": [
    "currency",
    "sha256"
  ],
  "type": "object",
  "title": "source_metadataArguments"
}
```
