"""Plantuml plugin tests.

make test T=test_plantuml.py
"""
from plantuml import PlantUML
from . import TestBase

UML_CODE = """
@startuml
Alice -> Bob: Hello Bob
Bob --> Alice: Hi!
@enduml
"""


class TesPlantuml(TestBase):
    """Plantuml content."""

    def _test_www(self):
        """Make image for plantuml content."""
        server = PlantUML(url='http://www.plantuml.com/plantuml/img/')
        image = server.processes(UML_CODE)
        assert len(image) > 0
        with open(self.build("test_plantuml.png"), "wb") as out:
            out.write(image)

    def test_md(self):
        """Process md with plantuml content."""
        from markdown_pdf import Section, MarkdownPdf, EXT_PLANTUML

        pdf = MarkdownPdf()
        assert not pdf.plugins
        text = open(self.fixture("plantuml.md"), "rt", encoding='utf-8').read()
        html = pdf.add_section(Section(text))
        assert "@startuml" in html
        pdf.save(self.build("plantuml.pdf"))

        pdf = MarkdownPdf(ext_plantuml="www")
        assert EXT_PLANTUML in pdf.plugins
