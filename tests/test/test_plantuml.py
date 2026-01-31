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

    def test_www(self):
        """Make image for plantuml content."""
        server = PlantUML(url='http://www.plantuml.com/plantuml/img/')
        image = server.processes(UML_CODE)
        assert len(image) > 0
        with open(self.build("test_plantuml.png"), "wb") as out:
            out.write(image)
