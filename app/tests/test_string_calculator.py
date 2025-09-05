from app.src.string_calculator import StringCalculator
import pytest

def test_string_calculator():
    calculator = StringCalculator()
    assert calculator.add('') == 0
    assert calculator.add('1') == 1

def test_string_calculator_many_numbers():
    calculator = StringCalculator()
    assert calculator.add('1,5') == 6
    assert calculator.add('2,5,3') == 10
    assert calculator.add('2,5,3,5') == 15
    assert calculator.add('2,5,3,') == 10

def test_calculator_with_newline_delimiter():
    calculator = StringCalculator()
    assert calculator.add('1\n5,5') == 11

def test_calculator_with_custom_delimiter():
    calculator = StringCalculator()
    assert calculator.add('//;\n1;2') == 3
    assert calculator.add('//:\n1:2:4') == 7
    assert calculator.add('//@\n5@5@5') == 15
    assert calculator.add('//aa\n2aa2aa2') == 6
    assert calculator.add('//;\n') == 0
    assert calculator.add('//***\n1***2***3') == 6

def test_calculator_with_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed -2,-4"):
        calculator = StringCalculator()
        calculator.add("1,-2,3,-4")


def test_calculator_with_numbers_gt_1k():
    calculator = StringCalculator()
    # numbers greater than 1000 should be ignored, 1000 is allowed
    assert calculator.add("1001, 2") == 2
    assert calculator.add("1000, 2") == 1002

def test_calculator_with_multiple_delimiters():
    calculator = StringCalculator()
    assert calculator.add("//[*][%]\n1*2%3") == 6
    assert calculator.add("//[*][%]\n1*2%3%") == 6
    assert calculator.add("//[***][%%]\n1***2%%3%%") == 6


def test_extra():
    calculator = StringCalculator()
    # empty delimiter
    assert calculator.add("//[]\n1231") == 7
    # double delimiter
    assert calculator.add("1,,2,3,1,") == 7
    assert calculator.add("//[*][**]\n1*2**3") == 6
