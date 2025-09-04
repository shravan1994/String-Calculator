from app.src.string_calculator import StringCalculator

def test_string_calculator():
    calculator = StringCalculator()
    assert calculator.add('') == 0
    assert calculator.add('1') == 1

def test_string_calculator_many_numbers():
    calculator = StringCalculator()
    assert calculator.add('1,5') == 6
    assert calculator.add('2,5,3') == 10
    assert calculator.add('2,5,3,5') == 15