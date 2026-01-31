"""Plantuml plugin tests.

make test T=test_plugins/test_plantuml.py
"""
from . import TestPlugin


class TestInit(TestPlugin):
    """Plantuml content."""

    def test_md(self):
        """Process md with plantuml content."""
        from markdown_pdf import Section, MarkdownPdf
        from markdown_pdf.pligins import Plugin

        pdf = MarkdownPdf()
        assert not pdf.plugins
        text = open(self.fixture("plantuml.md"), "rt", encoding='utf-8').read()
        html = pdf.add_section(Section(text))
        assert "@startuml" in html
        pdf.save(self.build("plantuml.pdf"))

        pdf = MarkdownPdf(ext_plantuml="www")
        assert Plugin.Plantuml in pdf.plugins
        text = open(self.fixture("plantuml.md"), "rt", encoding='utf-8').read()
        html = pdf.add_section(Section(text))
        assert "@startuml" in html
