from fuel import convert, guage
import pytest

def test_convert_integer():
    # Test cases to check if convert function correctly converts fractions to percentages
    assert convert('1/4') == 25  # 1 divided by 4 equals 0.25, which is 25%
    assert convert('3/4') == 75  # 3 divided by 4 equals 0.75, which is 75%
    assert convert('4/4') == 100  # 4 divided by 4 equals 1, which is 100%

def test_convert_zero():
    # Test case to check if convert function raises ZeroDivisionError for zero denominator
    with pytest.raises(ZeroDivisionError):
        convert('100/0')  # Division by zero should raise an error

def test_convert_type():
    # Test case to check if convert function raises ValueError for non-numeric input
    with pytest.raises(ValueError):
        convert('two/two')  # Non-numeric input should raise a ValueError

def test_gauge():
    # Test cases to check if gauge function returns correct fuel gauge reading
    assert guage(0.25) == 'E'  # Any percentage <= 1 should be 'E'
    assert guage(1) == 'E'  # Exactly 1% should be 'E'
    assert guage(100) == 'F'  # 100% should be 'F'
    assert guage(99) == 'F'  # 99% should be 'F'
    assert guage(45) == '45%'  # 45% should be '45%'
    assert guage(0) == 'E'  # 0% should be 'E'

