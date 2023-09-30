"""Pytest session setup."""
import sys
import os
import pytest


def path_setup():
    """Setup sys.path."""
    test_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(1, test_dir)


@pytest.fixture(scope="session", autouse=True)
def session_setup(request):
    """Auto session resource fixture."""
    path_setup()
