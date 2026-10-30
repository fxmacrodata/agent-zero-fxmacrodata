"""mcp_latest_announcements native Agent Zero tool."""

from usr.plugins.fxmacrodata.helpers import native


class FXMacroDataTool(native.PublicTool):
    operation = 'mcp_latest_announcements'
