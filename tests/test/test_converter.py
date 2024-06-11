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
        from markdown_pdf import Section, MarkdownPdf

        md = MarkdownIt('commonmark').enable('table')
        text = ("""
# Section with Table

|TableHeader1|TableHeader2|
|--|--|
|Text1|Text2|
|ListCell|<ul><li>FirstBullet</li><li>SecondBullet</li></ul>|
""")
        html_text = md.render(text)
        assert '<table>' in html_text

        pdf = MarkdownPdf(toc_level=0)
        pdf.add_section(Section(text))
        pdf.save(self.build("table.pdf"))
