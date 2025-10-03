from py_core.us128.conditional_logic import simple_if_else, multiple_conditions

def test_simple_if_else():
    assert simple_if_else(10) == "x is greater than 5"
    assert simple_if_else(5) == "x is not greater than 5"
    assert simple_if_else(-1) == "x is not greater than 5"

def test_multiple_conditions():
    assert multiple_conditions(95) == "Excellent"
    assert multiple_conditions(85) == "Pass"
    assert multiple_conditions(70) == "Fail"
    assert multiple_conditions(0) == "Fail"
