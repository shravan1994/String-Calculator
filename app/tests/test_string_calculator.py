from app.src.string_calculator import StringCalculator

def test_string_calculator():
    calculator = StringCalculator()
    assert calculator.add('') == 0
    assert calculator.add('1') == 1