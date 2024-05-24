from bank import value
def test_hello():
    # Test cases where the input string starts with "hello" in different formats
    assert value("Hello, everyone") == 0
    assert value("hello,everyonne") == 0

def test_h():
    # Test cases where the input string starts with "h" but not "hello"
    assert value("Hey, world") == 20
    assert value("hi, world") == 20

def test_without_hello():
    # Test cases where the input string does not start with "hello" or "h"
    assert value("Morning world") == 100
    assert value("what's up?") == 100
