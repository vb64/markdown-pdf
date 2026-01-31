"""Plugins."""
from .plantuml import handler as plantuml


class Plugin:
    """Available plugins."""

    Plantuml = "plantuml"


PLUGINS = {
  Plugin.Plantuml: plantuml,
}


def get_plugin_chunks(_key, _text):
    """Extract key parts from given text."""
    return []
