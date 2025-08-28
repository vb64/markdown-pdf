"""Package markdown_pdf tests.

make test T=test_converter.py
"""
import io
from . import TestBase

TABLE_TEXT = """# Section with Table

|TableHeader1|TableHeader2|
|--|--|
|Text1|Text2|
|ListCell|<ul><li>FirstBullet</li><li>SecondBullet</li></ul>|
"""


class TestConverter(TestBase):
    """Converter markdown_pdf."""

    def test_with_toc(self):
        """Convert md to pdf."""
        from markdown_pdf import Section, MarkdownPdf

        pdf = MarkdownPdf(toc_level=2)
        pdf.add_section(Section("# Title\n", toc=False))
        pdf.add_section(Section(TABLE_TEXT))
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

    def test_table(self):
        """Convert md table."""
        # https://github.com/executablebooks/markdown-it-py?tab=readme-ov-file#python-api-usage
        from markdown_it import MarkdownIt
        from markdown_pdf import Section, MarkdownPdf

        md = MarkdownIt('commonmark').enable('table')
        html_text = md.render(TABLE_TEXT)
        assert '<table>' in html_text

        pdf = MarkdownPdf(toc_level=0)
        pdf.add_section(Section(TABLE_TEXT))
        pdf.save(self.build("table.pdf"))

    def test_pathlib(self):
        """Check pathlib.Path for save method."""
        from pathlib import Path
        from markdown_pdf import MarkdownPdf, Section

        pdf = MarkdownPdf()
        pdf.add_section(Section('# Hello World'))

        file_path = Path(self.build('output.pdf'))
        pdf.save(file_path)

    def test_empty_head(self):
        """Check markdown with empty head."""
        from markdown_pdf import MarkdownPdf, Section

        pdf = MarkdownPdf(toc_level=2)
        pdf.add_section(Section("# "))
        pdf.save(self.build("empty-head.pdf"))

    def test_hrefs(self):
        """Convert hrefs content to pdf."""
        from markdown_pdf import Section, MarkdownPdf

        pdf = MarkdownPdf()
        pdf.add_section(
          Section(open(self.fixture("hrefs.md"), "rt", encoding='utf-8').read())
        )
        pdf.save(self.build("hrefs.pdf"))

    def test_bytes(self):
        """Save pdf as bytes IO."""
        from markdown_pdf import Section, MarkdownPdf
        out = io.BytesIO()

        pdf = MarkdownPdf(toc_level=2)
        pdf.add_section(Section("# Title Bytes\n", toc=False))
        pdf.add_section(Section("# Bytes1\n\nbody\n"))
        pdf.save_bytes(out)
        assert out.getbuffer().nbytes > 0
        with open(self.build("as_bytes.pdf"), "wb") as i:
            i.write(out.getvalue())
