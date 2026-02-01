"""Plantuml plugin tests.

make test T=test_plugins/test_init.py
"""
from . import TestPlugin, MockPlantUML


class TestInit(TestPlugin):
    """Plantuml content."""

    def test_md(self):
        """Process md with plantuml content."""
        from markdown_pdf import Section, MarkdownPdf, clear_temp_files
        from markdown_pdf.pligins import Plugin
        from markdown_pdf.pligins import plantuml

        pdf = MarkdownPdf()
        assert not pdf.plugins
        text = open(self.fixture("plantuml.md"), "rt", encoding='utf-8').read()
        html = pdf.add_section(Section(text))
        assert "@startuml" in html
        pdf.save(self.build("plantuml.pdf"))

        saved = plantuml.PlantUML
        plantuml.PlantUML = MockPlantUML

        plugins = {
          Plugin.Plantuml: {'url': 'http://www.plantuml.com/plantuml/img/'}
        }
        pdf = MarkdownPdf(plugins=plugins)
        assert Plugin.Plantuml in pdf.plugins
        text = open(self.fixture("plantuml.md"), "rt", encoding='utf-8').read()
        html = pdf.add_section(Section(text))
        assert "@startuml" not in html
        clear_temp_files(pdf.temp_files)

        plantuml.PlantUML = saved

    def test_get_plugin_chunks(self):
        """Check get_plugin_chunks function."""
        from markdown_pdf.pligins import Plugin, get_plugin_chunks

        text = open(self.fixture("plantuml.md"), "rt", encoding='utf-8').read()
        assert len(get_plugin_chunks(Plugin.Plantuml, text)) == 2
