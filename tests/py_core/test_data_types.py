import pytest
from py_core.us110.data_types import integer_operations, string_operations, boolean_evaluation

def test_integer_operations():
    result = integer_operations(6, 3)
    assert result["addition"] == 9
    assert result["subtraction"] == 3
    assert result["multiplication"] == 18
    assert result["division"] == 2
    # Division by zero
    result_zero = integer_operations(6, 0)
    assert result_zero["division"] == "Division by zero"

def test_string_operations():
    result = string_operations("abcde")
    assert result["concatenation"] == "abcdeabcde"
    assert result["slicing (first 3 chars)"] == "abc"

def test_boolean_evaluation():
    result = boolean_evaluation(5, 3)
    assert result["a == b"] is False
    assert result["a > b"] is True
    assert result["a < b"] is False
    result_equal = boolean_evaluation(4, 4)
    assert result_equal["a == b"] is True
    assert result_equal["a > b"] is False
    assert result_equal["a < b"] is False
