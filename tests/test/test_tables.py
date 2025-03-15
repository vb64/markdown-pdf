"""Tables related.

make test T=test_tables.py
"""
from . import TestBase


class TestTables(TestBase):
    """Tables content."""

    def test_table(self):
        """Convert table content to html."""
        from markdown_pdf import Section, MarkdownPdf

        text = """
I have some tables content in bellow, but after generate pdf file, table not appear.
| Description                    | Qty | Unit price | Amount    |
|-----------------------------|-----|------------|-----------|
| Premium Plan                   | 1   | €1,000.00  | €1,000.00 |
| May 24, 2025 – May 24, 2026    |     |            |           |
"""
        css = """
table {
width: 100%;
border-spacing: 0;
}

th, td {
border: 1px solid #d0d7de;
padding: 8px;
text-align: left;
}

tr {
border-bottom: 1px solid #d0d7de;
}

td {
background-clip: padding-box;
}
"""
        pdf = MarkdownPdf()
        pdf.add_section(Section(text), user_css=css)
        pdf.save(self.build("table_css.pdf"))
