"""Plugins."""
from .plantunl import handler as plantunl


class Plugin:
    """Available plugins."""

    Plantuml = "plantuml"


PLUGINS = {
  Plugin.Plantuml: plantunl,
}


def get_plugin_chunks(_key, _text):
    """Extract key part from given text."""
    return ""
