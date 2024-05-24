from plates import is_valid

def test_start():
    # Test cases where the plate starts with less than two letters
    assert bool(is_valid("A")) == False  # Single letter should be invalid
    assert bool(is_valid("A1")) == False  # Single letter followed by a digit should be invalid

def test_length():
    # Test case where the plate is longer than the maximum allowed length
    assert is_valid("Asd12345") == False  # Length exceeds typical plate length restrictions

def test_order():
    # Test cases checking the validity of the order of characters
    assert is_valid("CS50") == True  # Valid plate
    assert is_valid("CS05") == False  # Leading zeros in the number part should be invalid
    assert is_valid("AB2L") == False  # Numbers cannot be followed by letters

def test_punctuation():
    # Test cases where the plate contains punctuation or spaces
    assert is_valid("AS,34") == False  # Comma should make it invalid
    assert is_valid("AS3.14") == False  # Period should make it invalid
    assert is_valid("AS 312") == False  # Space should make it invalid