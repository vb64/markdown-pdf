"""Reproducibility tests.

Is it possible to create bit-by-bit identical pdfs from the same markdown input?

make test T=test_reproducible.py
"""
import hashlib
import pytest
from . import TestBase


def sha256_file(path: str) -> str:
    """Implement hashlib.file_digest for Python ver < 3.11."""
    h = hashlib.new("sha256")
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)

    return h.hexdigest()


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
        pdf.save(p1, no_new_id=True)
        pdf.save(p2, no_new_id=True)

        digest_1 = sha256_file(p1)
        digest_2 = sha256_file(p1)
        assert digest_1 == digest_2

        pdf.optimize = True
        with pytest.raises(ValueError) as err:
            pdf.save(p1, no_new_id=True)
        assert 'Cannot pass kwargs with optimize' in str(err.value)
