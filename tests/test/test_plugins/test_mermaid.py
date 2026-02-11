"""Mermaid plugin tests.

make test T=test_plugins/test_mermaid.py
"""
import base64
import requests
import pytest

from . import TestPlugin, MockRequsts

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

    @pytest.mark.external
    def test_www(self):
        """Make image for mermaid content."""
        # https://github.com/ouhammmourachid/mermaid-py
        response = requests.get(
          "https://mermaid.ink/img/{}".format(
            # Use URL-safe base64 encoding (replaces + with -, / with _)
            base64.urlsafe_b64encode(MERMAID_CODE.encode("utf-8")).decode("ascii"),
          ),
          params={"format": "png"},
          timeout=5
        )
        assert len(response.content) > 0
        with open(self.build("test_mermaid.png"), "wb") as out:
            out.write(response.content)

    @pytest.mark.external
    def test_plugin_use(self):
        """Make pdf with image for mermaid content."""
        from markdown_pdf import MarkdownPdf, Section
        from markdown_pdf.pligins import Plugin

        text = open(self.fixture("mermaid.md"), "rt", encoding='utf-8').read()
        plugins = {
          Plugin.Mermaid: None
        }

        pdf = MarkdownPdf(plugins=plugins)
        pdf.add_section(Section(text))
        pdf.save(self.build("test_mermaid.pdf"))

    def test_handler(self):
        """Check plugin handler."""
        from markdown_pdf.pligins import TempFiles, mermaid

        saved = mermaid.requests
        mermaid.requests = MockRequsts(content_from=self.fixture("mermaid.png"))

        temp_files = TempFiles()

        assert '[Mermaid image]' in mermaid.handler(None, "", temp_files)
        assert '[Mermaid image]' in mermaid.handler({'url': 'www'}, "", temp_files)

        temp_files.clean()
        mermaid.requests = saved
