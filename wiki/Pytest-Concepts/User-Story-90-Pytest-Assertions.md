# User Story 90: Pytest Assertions and Exceptions

## Overview
This user story demonstrates how to use Pytest for testing Python functions with assertions and for verifying that exceptions are raised as expected.

## Assertions in Pytest
Assertions are used to check that code returns the expected results. Pytest automatically interprets assert statements and provides clear output for both passing and failing tests.

**Example:**
```python
def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(2, 4) == 8  # This test will pass
```

## Testing Exceptions with pytest.raises
Pytest provides the pytest.raises context manager to check that a specific exception is raised during code execution. This is useful for verifying error handling in your code.

**Example:**
```python
import pytest

def divide(a, b):
    return a / b

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
```

## Summary
- Use assert statements to check for expected results in your tests.
- Use pytest.raises to verify that code raises the correct exceptions.
- Pytest provides clear output for both assertion failures and exception tests.

---
For more details, see 
 - the user story in [User Story 90: [Test] Using Assertions in pytest](https://dev.azure.com/gabriel-raby/Python/_workitems/edit/90)
 - the implementation in `math_ops.py` and `test_math_ops.py`
 - assertions documentation in [Pytest Assertions](https://docs.pytest.org/en/stable/how-to/assert.html)
 - exceptions documentation in [Pytest Exceptions](https://docs.pytest.org/en/stable/reference/reference.html#pytest-raises)