"""Test the add module."""

from uam.core import add


# test the add function
def test_add():
    """Test the add function."""
    assert add.add(1, 2) == 3
    assert add.add(1.5, 2.5) == 4


# test the add function with a string and expect a TypeError
def test_add_string():
    """Test the add function with a string and expect a TypeError."""
    try:
        add.add(1, "2")
    except TypeError:
        assert True
    else:
        assert False
