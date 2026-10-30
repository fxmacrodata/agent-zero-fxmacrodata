"""mcp_financial_prices native Agent Zero tool."""

from usr.plugins.fxmacrodata.helpers import native


class FXMacroDataTool(native.PublicTool):
    operation = 'mcp_financial_prices'
