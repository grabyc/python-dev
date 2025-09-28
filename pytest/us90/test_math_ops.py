import pytest
from math_ops import multiply, divide

def test_multiply():
    assert multiply(2, 4) == 8

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
