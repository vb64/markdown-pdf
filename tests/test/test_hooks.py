"""Hook tests.

https://pymupdf.readthedocs.io/en/latest/tutorial.html

make test T=test_hooks.py
"""
from . import TestBase


class TestHooks(TestBase):
    """Hooks tests."""

    def test_backcolor(self):
        """Check page background color feature."""
