"""Readme example code.

make test T=test_readme.py
"""
from . import TestBase


class TestReadme(TestBase):
    """Latex content."""

    def test_en(self):
        """Test README.md example code."""
        from markdown_pdf import Section, MarkdownPdf

        pdf = MarkdownPdf(toc_level=2, optimize=True)
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

    def test_user_case_1(self):
        """Test user case from discussion."""
        from markdown_pdf import Section, MarkdownPdf

        document_text_2 = """
# Test Header 0

Here's some background.

## Test Header 1

### 🗂️ Header 2 with hyperlink [link](http://www.example.com)

Some **Bold Text**

A lot more text here
"""

        document_text = "# Test Header 0\n"
        document_text += "\nHere's some background.\n"
        document_text += "\n## Test Header 1\n"
        document_text += "\n### 🗂️ Header 2 with hyperlink [link](http://www.example.com)\n"
        document_text += "Some **Bold Text**\n"
        document_text += "\nA lot more text here"

        pdf = MarkdownPdf(toc_level=2, optimize=True)
        pdf.add_section(Section(document_text, toc=False))
        pdf.save(self.build("rendered1.pdf"))

        pdf = MarkdownPdf(toc_level=2, optimize=True)
        pdf.add_section(Section(document_text_2, toc=False))
        pdf.save(self.build("rendered2.pdf"))
