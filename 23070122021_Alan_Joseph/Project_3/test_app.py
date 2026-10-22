from app import add, __version__


def test_add():
    assert add(1, 2) == 3


def test_version_is_set():
    assert __version__
