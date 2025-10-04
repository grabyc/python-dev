import pytest
from py_core.us129.looping_logic import for_loop_elements, while_loop_counter

def test_for_loop_elements():
    assert for_loop_elements([1, 2, 3]) == ['1', '2', '3']
    assert for_loop_elements([]) == []
    assert for_loop_elements(['a', 'b']) == ['a', 'b']

def test_while_loop_counter():
    assert while_loop_counter(0) == ['0', '1', '2']
    assert while_loop_counter(2) == ['2']
    assert while_loop_counter(3) == []
