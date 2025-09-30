import pytest
from py_core.us111.data_types_collections import list_operations, dict_access, tuple_immutability, set_uniqueness

def test_list_operations():
    # Append and remove
    result = list_operations([1, 2, 3], to_append=4, to_remove=2)
    assert result["final_list"] == [1, 3, 4]
    assert result["iteration"] == [1, 3, 4]
    # Remove non-existent
    result2 = list_operations([1, 2, 3], to_remove=5)
    assert result2["final_list"] == [1, 2, 3]

def test_dict_access():
    d = {"a": 1, "b": 2}
    assert dict_access(d, "a") == {"value": 1}
    assert dict_access(d, "c") == {"value": "Key not found"}

def test_tuple_immutability():
    t = (1, 2, 3)
    result = tuple_immutability(t, 1, 99)
    assert "tuples are immutable" in result["error"] or "does not support item assignment" in result["error"]

def test_set_uniqueness():
    values = [1, 2, 2, 3, 3, 3]
    result = set_uniqueness(values)
    assert set(result["unique_values"]) == {1, 2, 3}
