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

def test_calculator_with_newline_delimiter():
    calculator = StringCalculator()
    assert calculator.add('1\n5,5') == 11

def test_calculator_with_custom_delimiter():
    calculator = StringCalculator()
    calculator.add('//;\n1;2') == 3
    calculator.add('//:\n1:2:4') == 7
    calculator.add('//@\n5@5@5') == 15
    calculator.add('//aa\n2aa2aa2') == 6

def test_calculator_with_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed -2,-4"):
        calculator = StringCalculator()
        calculator.add("1,-2,3,-4")


def test_calculator_with_numbers_gt_1k():
    calculator = StringCalculator()
    # numbers greater than 1000 should be ignored
    assert calculator.add("1001, 2") == 2
