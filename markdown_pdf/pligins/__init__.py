"""Plugins."""
from .plantuml import handler as plantuml


class Plugin:
    """Available plugins."""

    Plantuml = "plantuml"


PLUGINS = {
  Plugin.Plantuml: plantuml,
}


def get_plugin_chunks(key, text):
    """Extract key parts from given text."""
    chunk = []
    chunks = []

    for line in text.splitlines():

        if line.startswith("```{}".format(key)):
            chunk = [line]
        elif (line.startswith("```")) and chunk:
            chunk.append(line)
            chunks.append('\n'.join(chunk))
            chunk = []
        elif chunk:
            chunk.append(line)

    return chunks
