from py_core.us125.mutability_logic import modify_list, modify_tuple, shared_reference_side_effects
import pytest

def test_modify_list():
    lst = [1, 2, 3]
    result = modify_list(lst, 4)
    assert result == [1, 2, 3, 4]
    # Ensure original list is modified (mutability)
    assert lst == [1, 2, 3, 4]

def test_modify_tuple():
    tpl = (1, 2, 3)
    # Should raise TypeError message
    error = modify_tuple(tpl, 0, 9)
    assert "does not support item assignment" in error or "'tuple' object does not support item assignment" in error

def test_shared_reference_side_effects():
    a, b = shared_reference_side_effects()
    assert a == [10, 20, 30]
    assert b == [10, 20, 30]
    assert a is b
