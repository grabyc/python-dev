from py_core.us124.type_conversion_logic import implicit_conversion, explicit_conversion, conversion_error
import pytest

def test_implicit_conversion():
    result = implicit_conversion(2, 3.5)
    assert result == 5.5
    assert isinstance(result, float)

def test_explicit_conversion():
    assert explicit_conversion("42") == 42
    assert isinstance(explicit_conversion("42"), int)
    with pytest.raises(ValueError):
        int("abc")

def test_conversion_error():
    # Should return error message for invalid string
    error = conversion_error("abc")
    assert "invalid literal" in error
    # Should return int for valid string
    assert conversion_error("42") == 42
