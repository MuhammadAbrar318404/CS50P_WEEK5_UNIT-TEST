
from twttr import shorten

def test_upper_lower():
    # Test the shorten function with all uppercase input
    assert shorten("ABRAR IS A GOOD ENGINEER") == "BRR S  GD NGNR"
    # Test the shorten function with all lowercase input
    assert shorten("abrar is a good engineer") == "brr s  gd ngnr"
    # Test the shorten function with mixed case input
    assert shorten("Abrar is a gooD Engineer") == "brr s  gD ngnr"

def test_numbers():
    # Test the shorten function with numerical input
    assert shorten("12345") == "12345"
    # Test the shorten function with numerical input containing punctuation
    assert shorten("123.45") == "123.45"

def test_punctuation():
    # Test the shorten function with input containing punctuation
    assert shorten("Abrar's car is 'broken'") == "brr's cr s 'brkn'"

