"""Latex content tests.

make test T=test_latex.py
"""
# pylint: disable=line-too-long
from . import TestBase

LATEX_CSS = """
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });</script>
"""


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

    def test_latex_css(self):
        """Convert latext content to pdf with css."""
        from markdown_pdf import Section, MarkdownPdf

        pdf = MarkdownPdf()
        pdf.add_section(
          Section(open(self.fixture("latex2.md"), "rt", encoding='utf-8').read()),
          user_css=LATEX_CSS
        )
        pdf.save(self.build("latex2.pdf"))
