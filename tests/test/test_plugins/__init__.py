"""Root class for testing plugins."""
from plantuml import PlantUMLConnectionError
from .. import TestBase


class MockPlantUML:
    """Mocked PlantUML class."""

    def __init__(self, url=''):
        """Make new instance."""
        self.url = url

    def processes(self, _text):
        """Emulate call."""
        if not self.url.startswith('http://'):
            raise PlantUMLConnectionError("Only absolute URIs are allowed.")

        return open("fixture/plantuml.png", "rb").read()


class TestPlugin(TestBase):
    """Base class for tests plugins."""
