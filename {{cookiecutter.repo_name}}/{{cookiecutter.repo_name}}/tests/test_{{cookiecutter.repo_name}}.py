"""
Unit and regression test for the {{cookiecutter.repo_name}} package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import {{cookiecutter.repo_name}}


def test_{{cookiecutter.repo_name}}_imported():
    """Sample test, will always pass so long as import statement worked."""
    print("importing ", {{cookiecutter.repo_name}}.__name__)
    assert "{{cookiecutter.repo_name}}" in sys.modules


# Assert that a certain exception is raised
def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
