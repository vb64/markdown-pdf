"""Package markdown_pdf tests.

make test T=test_converter.py
"""
from . import TestBase


class TestConverter(TestBase):
    """Converter markdown_pdf."""

    def test_with_toc(self):
        """Convert md to pdf."""
        from markdown_pdf import Section, MarkdownPdf

        pdf = MarkdownPdf(toc_level=2)
        pdf.add_section(Section("# Title\n", toc=False))
        pdf.add_section(
          Section("# Head1\n\n![python](img/python.png)\n\nbody\n"),
          user_css="h1 {text-align:center;}"
        )
        pdf.add_section(Section("## Head2\n\n### Head3\n\n"))
        pdf.save(self.build("with_toc.pdf"))

    def test_no_toc(self):
        """Convert md to pdf."""
        from markdown_pdf import Section, MarkdownPdf

        pdf = MarkdownPdf(toc_level=0)
        pdf.add_section(Section("# Title\n"))
        pdf.save(self.build("no_toc.pdf"))

    def test_table_html(self):
        """Convert md table to html."""

        # https://github.com/executablebooks/markdown-it-py?tab=readme-ov-file#python-api-usage
        from markdown_it import MarkdownIt
        from mdit_py_plugins.front_matter import front_matter_plugin
        from mdit_py_plugins.footnote import footnote_plugin
        # from pathlib import Path

        md = (
          MarkdownIt('commonmark', {'breaks': True, 'html': True})
          .use(front_matter_plugin)
          .use(footnote_plugin)
          .enable('table')
        )

        text = ("""
---
a: 1
---

a | b
- | -
1 | 2

A footnote [^1]

[^1]: some details
""")
        html_text = md.render(text)
        print("\n")
        print(html_text)
        # Path(self.build("table.html")).write_text(html_text)
