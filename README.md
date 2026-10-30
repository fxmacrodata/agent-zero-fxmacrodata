# FXMacroData for Agent Zero

Official-source macroeconomic research in Agent Zero: release calendars, indicator histories, FX/reference rates, commodities, COT positioning and central-bank analysis.98 schema-aware native tools reuse FXMacroData's hosted product; no data feed or service implementation is packaged.

[Explore FXMacroData](https://fxmacrodata.com/?utm_source=agent-zero&utm_medium=integration&utm_campaign=agent-zero-fxmacrodata&utm_content=readme) · [Documentation](https://fxmacrodata.com/documentation/reference?utm_source=agent-zero&utm_medium=integration&utm_campaign=agent-zero-fxmacrodata&utm_content=docs)

## Installation and discovery

Source/package releases and Plugin Hub acceptance are separate. Check Agent Zero's Plugin Hub for the accepted listing; once listed, install FXMacroData there and enable it for the intended scope. The plugin belongs in `usr/plugins/fxmacrodata`, with plugin.yaml at its root. Do not treat a local package as a live marketplace listing.

Installation/update hooks check the host's existing Python dependencies. They do not install packages, run subprocesses, download code, write credentials or start services. A supported host must provide pydantic2, jsonschema4, requests2 and referencing. A missing dependency fails clearly; no manual Execute action is required. The client is vendored with its license and provenance; there is no pinned remote wheel download.

## Public USD evaluation

Leave the process API-key environment variables unset to use public USD evaluation. Start with `fxmd_data_catalogue` and the exact schema in its prompt, then request a bounded recent USD history or release calendar. Public access may be delayed and limited to a recent window; pass notices through to the user. Discover indicator slugs before history requests. No model step or automatic background data download is included.

## Optional subscriber access

In plugin settings, enter only the environment-variable name containing your own FXMacroData key (default FXMACRODATA_API_KEY; legacy FXMD_API_KEY fallback). Set the value through the host's existing secret/environment configuration, never a prompt, project document, public URL or tool arguments. This is process-environment access, not a claim of per-user credential isolation. A multi-user deployment must establish its own secret boundaries before supplying paid access. Plugin config holds the variable name and timeouts only. The client sends header-based authentication, rejects unsafe keys and endpoint overrides, and does not follow redirects.

The plugin code is MIT licensed. FXMacroData dataset entitlements are separate. Agent Zero model/API/hosting costs are separate from free plugin code and any Plugin Hub listing. No plan, paid model, publisher account or billing permission is provisioned by this plugin.

## Outputs and limits

Each result preserves the public response in data, a records convenience view and source_url. These are alternative views, not additional observations. Follow pagination explicitly; one response is not a full-series export. The stream tool is a bounded snapshot, not a persistent subscription. Structured MCP resources are retained; interactive MCP Apps iframe rendering is not supplied. Missing observations never become zero. Publication, scheduled and ingestion clocks remain distinct; absent evidence and latency are unknown. Own forecasts are labelled.

Arguments retain JSON Schema types, required fields, nesting and enums. Errors do not expose request credentials. Model arguments are omitted from pre-execution logs. Request concurrency and timeouts are bounded. Cancellation stops awaiting; in-flight synchronous requests drain under their HTTP timeout and close their clients.

## Updates and removal

Disable the plugin in Agent Zero and uninstall through its native controls. The plugin owns no services, installed dependencies, scheduled jobs or persistent data; uninstall leaves shared dependencies, environment secrets and unrelated user data untouched. Rotate/remove your key through your normal secret management if desired.

See CAPABILITIES.md for the complete98-tool inventory and NOTICE.txt for reused public-client provenance. Native test results distinguish mocked external transport from live service execution and full application UI acceptance.

## Native validation

Validated with the official Agent Zero runtime image, pinned by digest, using its framework Python3.12.4. The real framework discovered the plugin and configuration screen, loaded all98 native tools, and completed196 tool/client executions across public and synthetic-key modes with HTTP fixtures. Real AgentContext/Agent creation, scoped settings, logging/history, install/update hooks, disable/re-enable and native uninstall passed. Uninstall preserved unrelated test state and shared dependencies.

Bounded anonymous native acceptance also passed REST health, MCP capabilities and a one-row recent USD policy-rate history request: five HTTP requests total, no model requests or credentials. The separate owned suite passes221 offline checks. Structured resources are preserved, but interactive MCP Apps rendering and visual settings-page interaction are outside these checks.

The runtime image is `agent0ai/agent-zero@sha256:307a2ceffc8501ba05a1e7253e8b6e4d656d2e1c3b97f0eb943c18b9c40a30fd`. The runtime was tested with no host mounts, no browser process, no paid account and no extra account permissions. Its tokenizer data was cached from the official source after verifying the package's expected hash, then native offline checks ran with networking disabled.
