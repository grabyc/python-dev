# User Story 89: Pytest Basics

## Overview
This user story demonstrates the basics of using the Pytest library for testing Python code. Pytest is a powerful and easy-to-use testing framework that allows you to write simple test functions and use assertions to verify code behavior.

## Writing Tests with Pytest
Pytest discovers test files and functions automatically. Test functions should be named with the prefix `test_`.

**Example:**
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5  # This test will pass

def test_add_fail():
    assert add(2, 3) == 6  # This test will fail
```

## Running Tests
To run all tests in the current directory, use:
```bash
pytest
```
Pytest will show which tests passed and which failed, along with clear error messages for failures.

## Assertions
Assertions are used to check that code returns expected results. If an assertion fails, Pytest reports the failure and shows the expected vs. actual values.

## Summary
- Pytest makes it easy to write and run tests for Python code.
- Use assertions to verify code correctness.
- Pytest provides clear output for both passing and failing tests.

---
For more details, see 
 - the user story in [User Story 89: [Test] Writing Simple Tests with pytest](https://dev.azure.com/gabriel-raby/Python/_workitems/edit/89)
 - the implementation in `add.py` and `test_add.py`
 - assertions documentation in [Pytest Assertions](https://docs.pytest.org/en/stable/how-to/assert.html)

