"""Latex content tests.

make test T=test_latex.py
"""
from . import TestBase


class TestLatex(TestBase):
    """Latex content."""

    def test_latex(self):
        """Convert latext content to html."""
        from markdown_pdf import Section, MarkdownPdf

        pdf = MarkdownPdf()
        text = open(self.fixture("latex1.md"), "rt", encoding='utf-8').read()
        html = pdf.add_section(Section(text))
        # print(html)
        assert "$$" in html
