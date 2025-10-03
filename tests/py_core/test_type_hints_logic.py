from py_core.us112.type_hints_logic import add, sum_list
import pytest

def test_add_valid():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_add_type_error():
    with pytest.raises(TypeError):
        add("2", 3)  # type: ignore


def test_sum_list_valid():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0


def test_sum_list_type_error():
    with pytest.raises(TypeError):
        sum_list([1, "2", 3])  # type: ignore
