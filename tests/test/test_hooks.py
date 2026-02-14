"""Hook tests.

https://pymupdf.readthedocs.io/en/latest/tutorial.html

make test T=test_hooks.py
"""
import fitz
from . import TestBase


class TestHooks(TestBase):
    """Hooks tests."""

    def test_backcolor(self):
        """Check page background color feature."""
        from markdown_pdf import Section, MarkdownPdf

        pdf = MarkdownPdf()
        text = open(self.fixture("plantuml.md"), "rt", encoding='utf-8').read()
        section = Section(text)

        where = section.rect + section.borders
        html = pdf.m_d.render(section.text)
        story = fitz.Story(html=html, archive=section.root)

        page = pdf.writer.begin_page(section.rect)

        # https://pymupdf.readthedocs.io/en/latest/the-basics.html#adding-a-watermark-to-a-pdf
        # insert an image watermark from a file name to fit the page bounds
        # page.insert_image(page.bound(), filename="watermark.png", overlay=False)
        # https://pypi.org/project/pypng/

        story.place(where)
        # story.element_positions(self._recorder, {"toc": section.toc, "pdfile": self})
        story.draw(page)
        pdf.writer.end_page()

        pdf.save(self.build('backcolor.pdf'))
