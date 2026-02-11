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


class MockResponse:
    """Mocked requests response."""

    def __init__(self, content=None):
        """Make new response."""
        self.content = content


class MockRequsts:
    """Mocked requests lib."""

    def __init__(self, content_from=None):
        """Make new requests session."""
        self.content_from = content_from
        self.url = None
        self.params = None
        self.timeout = None

    def get(self, url, params=None, timeout=None):
        """Mock get method."""
        self.url = url
        self.params = params
        self.timeout = timeout

        return MockResponse(content=open(self.content_from, mode='rb').read())


class TestPlugin(TestBase):
    """Base class for tests plugins."""
