"""Plugins."""
import os
import uuid

from .plantuml import handler as plantuml_handler

PLUGINS = {}


class Plugin:
    """Available plugins."""

    Plantuml = "plantuml"


class TempFiles:
    """Temp files for plugins."""

    def __init__(self):
        """Init empty list."""
        self.name_list = []

    def new_name(self, ext=None):
        """Return file name with given extension."""
        self.name_list.append(str(uuid.uuid4()) + ".{}".format(ext) if ext else '')
        return self.name_list[-1]

    def clean(self):
        """Remove temp files."""
        for i in self.name_list:
            if os.path.exists(i):
                os.remove(i)


def register_plugin(key, handler):
    """Register plugin as available."""
    PLUGINS[key] = handler


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


register_plugin(Plugin.Plantuml, plantuml_handler)
