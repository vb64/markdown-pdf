"""Plantuml plugin tests.

make test T=test_plugins/test_plantuml.py
"""
import pytest
from plantuml import PlantUML, PlantUMLConnectionError
from . import TestPlugin

UML_CODE = """
@startuml
Alice -> Bob: Hello Bob
Bob --> Alice: Hi!
@enduml
"""


class TesPlantuml(TestPlugin):
    """Plantuml content."""

    def _test_www(self):
        """Make image for plantuml content."""
        server = PlantUML(url='http://www.plantuml.com/plantuml/img/')
        image = server.processes(UML_CODE)
        assert len(image) > 0
        with open(self.build("test_plantuml.png"), "wb") as out:
            out.write(image)

    def test_handler(self):
        """Check handler function."""
        from markdown_pdf.pligins import get_plugin_chunks, Plugin
        from markdown_pdf.pligins import plantuml

        text = open(self.fixture("plantuml.md"), "rt", encoding='utf-8').read()
        text = get_plugin_chunks(Plugin.Plantuml, text)[0]
        temp_files = []
        params = {}
        chunk = plantuml.handler(params, text, temp_files)
        assert "No value for 'url'" in chunk

        params = {'url': 'www'}
        with pytest.raises(PlantUMLConnectionError) as exp:
            plantuml.handler(params, text, temp_files)
        assert "Only absolute URIs are allowed." in str(exp)

        params['url'] = 'http://www.plantuml.com/plantuml/img/'
        chunk = plantuml.handler(params, text, temp_files)
        assert ".png" in chunk
