"""Reproducibility tests.

Is it possible to create bit-by-bit identical pdfs from the same markdown input?

make test T=test_reproducible.py
"""
import hashlib
from . import TestBase


def sha256_file(path: str) -> str:
    """Implement hashlib.file_digest for Python ver < 3.11."""
    h = hashlib.new("sha256")
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)

    return h.hexdigest()


def check_no_new_id(pdf, p1, p2):
    """Check no_new_id arg is working."""
    pdf.save(p1, no_new_id=True)
    pdf.save(p2, no_new_id=True)
    assert sha256_file(p1) == sha256_file(p2)

    pdf.save(p1, no_new_id=False)
    pdf.save(p2, no_new_id=False)
    assert sha256_file(p1) != sha256_file(p2)


class TestReproducibility(TestBase):
    """Reproducibility tests."""

    def test_reproducibility(self):
        """Check bit-by-bit identical pdf saves from same markdown input."""
        from markdown_pdf import MarkdownPdf, Section

        p1 = self.build("hello1.pdf")
        p2 = self.build("hello2.pdf")

        pdf = MarkdownPdf()

        pdf.meta["creationDate"] = ""
        pdf.meta["modDate"] = ""
        txt = "Hello World"
        pdf.add_section(Section(txt))

        assert not pdf.optimize
        check_no_new_id(pdf, p1, p2)

        pdf.optimize = True
        check_no_new_id(pdf, p1, p2)
