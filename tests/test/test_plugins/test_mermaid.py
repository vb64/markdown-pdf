"""Mermaid plugin tests.

make test T=test_plugins/test_mermaid.py
"""
import base64
from urllib.parse import urlencode
import requests

from . import TestPlugin

MERMAID_CODE = """
stateDiagram-v2
    [*] --> Still
    Still --> [*]

    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
"""


class TesMermaid(TestPlugin):
    """Mermaid content."""

    def test_www(self):
        """Make image for mermaid content."""
        # https://github.com/ouhammmourachid/mermaid-py
        response = requests.get(
          "https://mermaid.ink/img/{}?{}".format(
            # Use URL-safe base64 encoding (replaces + with -, / with _)
            base64.urlsafe_b64encode(MERMAID_CODE.encode("utf-8")).decode("ascii"),
            urlencode({"format": "png"}, doseq=True)
          ),
          timeout=5
        )
        assert len(response.content) > 0
        with open(self.build("test_mermaid.png"), "wb") as out:
            out.write(response.content)
