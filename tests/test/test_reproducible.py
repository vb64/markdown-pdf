"""
Reproducibility tests.

Is it possible to create bit-by-bit identical pdfs from the same markdown
input?

make test T=test_reproducible.py

"""

from . import TestBase

class TestReproducibility(TestBase):
    """Reproducibility tests."""

    def test_reproducibility(self):
        """Check bit-by-bit identical pdf saves from same markdown input."""
        import hashlib
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

        with open(p1, "rb") as f, open(p2, "rb") as ff:
            digest_f = hashlib.file_digest(f, "sha256")
            digest_ff = hashlib.file_digest(ff, "sha256")
            self.assertEqual(digest_f.hexdigest(), digest_ff.hexdigest())

        pdf.optimize = True
        with self.assertRaises(ValueError):
            pdf.save(p1, no_new_id=True)
