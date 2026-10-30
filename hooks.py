"""Read-only lifecycle checks; no package manager, network or process writes."""
from importlib import metadata


def install():
    """Check host-provided dependencies on install/update, without installing."""
    supported = {"pydantic": 2, "jsonschema": 4, "requests": 2, "referencing": 0}
    for name, major in supported.items():
        try:
            installed = metadata.version(name)
            if int(installed.split(".")[0]) != major:
                raise ValueError("unsupported major")
        except (metadata.PackageNotFoundError, ValueError):
            raise RuntimeError("FXMacroData requires a supported Agent Zero host with pydantic2, jsonschema4, requests2 and referencing. No dependency changes were made.") from None


def uninstall():
    """There are no plugin-owned services, dependencies or data to remove."""
    return None
