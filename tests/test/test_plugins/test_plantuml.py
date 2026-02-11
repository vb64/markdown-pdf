"""Plantuml plugin tests.

make test T=test_plugins/test_plantuml.py
"""
import pytest
from plantuml import PlantUML, PlantUMLConnectionError
from . import TestPlugin, MockPlantUML

UML_CODE = """
@startuml
Alice -> Bob: Hello Bob
Bob --> Alice: Hi!
@enduml
"""


class TesPlantuml(TestPlugin):
    """Plantuml content."""

    @pytest.mark.external
    def test_www(self):
        """Make image for plantuml content."""
        server = PlantUML(url='http://www.plantuml.com/plantuml/img/')
        image = server.processes(UML_CODE)
        assert len(image) > 0
        with open(self.build("test_plantuml.png"), "wb") as out:
            out.write(image)

    @pytest.mark.external
    def test_plugin_use(self):
        """Make pdf with image for plantuml content."""
        from markdown_pdf import MarkdownPdf, Section
        from markdown_pdf.pligins import Plugin

        text = open(self.fixture("plantuml.md"), "rt", encoding='utf-8').read()
        plugins = {
          Plugin.Plantuml: {'url': 'http://www.plantuml.com/plantuml/img/'}
        }

        pdf = MarkdownPdf(plugins=plugins)
        pdf.add_section(Section(text))
        pdf.save(self.build("test_plantuml.pdf"))

    def test_handler(self):
        """Check handler function."""
        from markdown_pdf import TempFiles
        from markdown_pdf.pligins import get_plugin_chunks, Plugin
        from markdown_pdf.pligins import plantuml

        saved = plantuml.PlantUML
        plantuml.PlantUML = MockPlantUML

        text = open(self.fixture("plantuml.md"), "rt", encoding='utf-8').read()
        text = get_plugin_chunks(Plugin.Plantuml, text)[0]
        temp_files = TempFiles()
        params = {}
        chunk = plantuml.handler(params, text, temp_files)
        assert "[PlantUML image]" in chunk

        params = {'url': 'www'}
        with pytest.raises(PlantUMLConnectionError) as exp:
            plantuml.handler(params, text, temp_files)
        assert "Only absolute URIs are allowed." in str(exp)

        params['url'] = 'http://www.plantuml.com/plantuml/img/'
        chunk = plantuml.handler(params, text, temp_files)
        assert ".png" in chunk
        temp_files.clean()

        plantuml.PlantUML = saved
