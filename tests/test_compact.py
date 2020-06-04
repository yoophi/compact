from compact import __version__
from compact import compact


def test_version():
    assert __version__ == '0.1.0'

def test_single_args():
    a = 1
    assert {"a": 1} == compact("a")

def test_multiple_args():
    hello = "hello"
    world = 42
    assert {"hello": hello, "world": world} \
         == compact("hello", "world")