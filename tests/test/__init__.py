"""Root class for testing."""
import os
from unittest import TestCase


class TestBase(TestCase):
    """Base class for tests."""

    @staticmethod
    def fixture(*file_name):
        """Return path to fixture file."""
        return os.path.join('fixture', *file_name)

    @staticmethod
    def build(*file_name):
        """Return path to file in 'build' folder."""
        return os.path.join('build', *file_name)
