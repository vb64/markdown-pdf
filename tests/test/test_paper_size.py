"""Package markdown_pdf tests.

make test T=test_paper_size.py
"""
import pytest

from . import TestBase


class TestPaperSize(TestBase):
    """Section paper_size validation."""

    def test_paper_size_list_and_tuple_ok(self):
        """Valid two-element sizes keep working."""
        from markdown_pdf import Section

        Section("# Hi", paper_size=[210, 297])
        Section("# Hi", paper_size=(210, 297))

    def test_paper_size_wrong_length(self):
        """Sizes with != 2 elements fail with a clear error."""
        from markdown_pdf import Section

        with pytest.raises(TypeError, match="exactly 2 elements"):
            Section("# Hi", paper_size=[210, 297, 100])
        with pytest.raises(TypeError, match="exactly 2 elements"):
            Section("# Hi", paper_size=[])
        with pytest.raises(TypeError, match="exactly 2 elements"):
            Section("# Hi", paper_size=(210,))
