"""intraday_reference_rates native Agent Zero tool."""

from usr.plugins.fxmacrodata.helpers import native


class FXMacroDataTool(native.PublicTool):
    operation = 'intraday_reference_rates'
