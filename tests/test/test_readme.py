"""Readme example code.

make test T=test_readme.py
"""
from . import TestBase


class TestReadme(TestBase):
    """Latex content."""

    def test_en(self):
        """Test README.md example code."""
        from markdown_pdf import Section, MarkdownPdf

        pdf = MarkdownPdf(toc_level=2)
        pdf.add_section(Section("# Title\n", toc=False))

        text = """# Section with links

- [External link](https://github.com/vb64/markdown-pdf)
- [Internal link to Head1](#head1)
- [Internal link to Head3](#head3)
"""
        pdf.add_section(Section(text))

        pdf.add_section(
          Section("# <a name='head1'></a>Head1\n\n![python](img/python.png)\n\nbody\n"),
          user_css="h1 {text-align:center;}"
        )
        pdf.add_section(Section("## Head2\n\n### <a id='head3'></a>Head3\n\n", paper_size="A4-L"))
        text = """# Section with Table

|TableHeader1|TableHeader2|
|--|--|
|Text1|Text2|
|ListCell|<ul><li>FirstBullet</li><li>SecondBullet</li></ul>|
"""
        css = "table, th, td {border: 1px solid black;}"
        pdf.add_section(Section(text), user_css=css)

        pdf.meta["title"] = "User Guide"
        pdf.meta["author"] = "Vitaly Bogomolov"

        pdf.save(self.build("readme.pdf"))
