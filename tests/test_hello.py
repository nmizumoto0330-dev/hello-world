import pytest
from hello import greet, farewell


def test_greet_basic():
    assert greet("World") == "Hello, World!"


def test_greet_name():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty_raises():
    with pytest.raises(ValueError):
        greet("")


def test_farewell_basic():
    assert farewell("World") == "Goodbye, World!"


def test_farewell_empty_raises():
    with pytest.raises(ValueError):
        farewell("")


def test_greet_japanese():
    assert greet("田中", lang="ja") == "こんにちは、田中！"


def test_farewell_japanese():
    assert farewell("田中", lang="ja") == "さようなら、田中！"
