"""Markdown to pdf converter based on markdown_it and fitz."""
import io
import typing
import pathlib

import fitz
from markdown_it import MarkdownIt
from pymupdf import (
  _as_pdf_document, mupdf, JM_embedded_clean, JM_ensure_identity, JM_new_output_fileptr, ASSERT_PDF, Rect,
)

MM_2_PT = 2.835


class Section:
    """Markdown section."""

    def __init__(
      self,
      text: str,
      toc: bool = True,
      root: str = ".",
      paper_size: str or list or tuple = "A4",
      borders: typing.Tuple[int, int, int, int] = (36, 36, -36, -36)
    ):
        """Create md section with given properties."""
        self.text = text
        self.toc = toc
        self.root = root

        self.paper_size = paper_size
        if isinstance(paper_size, str):
            # https://pymupdf.readthedocs.io/en/latest/functions.html#paper_size
            self.rect = fitz.paper_rect(paper_size)
        elif isinstance(paper_size, (list, tuple)):
            # Other paper sizes are in pt, so need to times mm by 2.835.
            width, height = paper_size
            self.rect = Rect(0.0, 0.0, (width * MM_2_PT), (height * MM_2_PT))
        else:
            raise TypeError("paper_size must be 'str', 'tuple' or 'list'")

        self.borders = borders


class MarkdownPdf:
    """Converter class."""

    meta = {
      "creationDate": fitz.get_pdf_now(),
      "modDate": fitz.get_pdf_now(),
      "creator": "PyMuPDF library: https://pypi.org/project/PyMuPDF",
      "producer": None,
      "title": None,
      "author": None,
      "subject": None,
      "keywords": None,
    }

    def __init__(self, toc_level: int = 6, mode: str = 'commonmark', optimize: bool = False):
        """Create md -> pdf converter with given TOC level and mode of md parsing."""
        self.toc_level = toc_level
        self.toc = []

        # zero, commonmark, js-default, gfm-like
        # https://markdown-it-py.readthedocs.io/en/latest/using.html#quick-start
        self.m_d = (MarkdownIt(mode).enable('table'))  # Enable support for tables

        self.optimize = optimize

        self.out_file = io.BytesIO()
        self.writer = fitz.DocumentWriter(self.out_file)
        self.page_num = 0
        self.hrefs = []

    @staticmethod
    def _recorder(elpos):
        """Call function invoked during story.element_positions() for making a TOC and hrefs."""
        elpos.page_num = elpos.pdfile.page_num
        elpos.pdfile.hrefs.append(elpos)

        if not elpos.open_close & 1:  # only consider "open" items
            return
        if not elpos.toc:
            return

        if 0 < elpos.heading <= elpos.pdfile.toc_level:  # this is a header (h1 - h6)
            elpos.pdfile.toc.append((
                elpos.heading,
                elpos.text,
                elpos.pdfile.page_num,
                elpos.rect[1],  # top of written rectangle (use for TOC)
            ))

    def add_section(self, section: Section, user_css: typing.Optional[str] = None) -> str:
        """Add markdown section to pdf."""
        where = section.rect + section.borders
        html = self.m_d.render(section.text)
        story = fitz.Story(html=html, archive=section.root, user_css=user_css)
        more = 1
        while more:  # loop outputting the story
            self.page_num += 1
            device = self.writer.begin_page(section.rect)
            more, _ = story.place(where)  # layout into allowed rectangle
            story.element_positions(self._recorder, {"toc": section.toc, "pdfile": self})
            story.draw(device)
            self.writer.end_page()

        return html

    def _make_doc(self):
        """Return fitz doc object."""
        self.writer.close()
        self.out_file.seek(0)
        doc = fitz.Story.add_pdf_links(self.out_file, self.hrefs)
        doc.set_metadata(self.meta)
        if self.toc_level > 0:
            doc.set_toc(self.toc)

        return doc

    def save(self, file_name: typing.Union[str, pathlib.Path]) -> None:
        """Save pdf to file."""
        doc = self._make_doc()
        if self.optimize:
            doc.ez_save(file_name)
        else:
            doc.save(file_name)
        doc.close()

    def save_bytes(self, bytesio: io.BytesIO) -> int:
        """Save pdf to file-like object and return byte size of the filled object."""
        doc = self._make_doc()

        pdf = _as_pdf_document(doc)
        opts = mupdf.PdfWriteOptions()

        opts.do_incremental = 0
        opts.do_ascii = 0
        opts.do_compress = 0
        opts.do_compress_images = 0
        opts.do_compress_fonts = 0
        opts.do_decompress = 0
        opts.do_garbage = 0
        opts.do_pretty = 0
        opts.do_linear = 0
        opts.do_clean = 0
        opts.do_sanitize = 0
        opts.dont_regenerate_id = 0
        opts.do_appearance = 0
        opts.do_encrypt = 1
        opts.permissions = 4095
        opts.do_preserve_metadata = 1
        opts.do_use_objstms = 0
        opts.compression_effort = 0

        ASSERT_PDF(pdf)
        pdf.m_internal.resynth_required = 0
        JM_embedded_clean(pdf)
        JM_ensure_identity(pdf)

        out = JM_new_output_fileptr(bytesio)
        mupdf.pdf_write_document(pdf, out, opts)
        out.fz_close_output()

        return bytesio.getbuffer().nbytes
