# User Story 112: Python Type Hints and Annotations

## Overview
This user story demonstrates the use of type hints and annotations in Python. Type hints help document code, enable static analysis, and catch type errors before runtime using tools like mypy or IDEs.

## Function Parameter and Return Type Hints
Type hints specify the expected types of function parameters and return values. This improves code readability and helps static analyzers catch type mismatches.

**Example:**
```python
def add(a: int, b: int) -> int:
    return a + b
```
- Passing integers works as expected.
- Passing a string (e.g., add("2", 3)) will be flagged by static checkers.

## Complex Type Hints
You can annotate more complex types, such as lists of integers, using the typing module or built-in generics (Python 3.9+).

**Example:**
```python
from typing import List

def sum_list(numbers: list[int]) -> int:
    return sum(numbers)
```
- Passing a list of integers is accepted.
- Passing a list with non-integers will be flagged by static checkers.

## Type Checking Tools
- **mypy** and modern IDEs can check your code for type mismatches based on annotations.
- Type hints do not enforce types at runtime, but help catch errors early during development.

## Summary
- Type hints improve code clarity and enable static analysis.
- Use type annotations for function parameters, return values, and complex types.
- Static checkers like mypy help catch type errors before runtime.

---
For more details, see 
 - the user story in [User Story 112: [Data Types] Applying Type Hints & Annotations](https://dev.azure.com/gabriel-raby/Python/_workitems/edit/112)
 - the implementation in `type_hints_logic.py` and `gradio_app.py` 
 - type hints documentation in 
    - [RealPython Type Hints](https://realpython.com/python-type-checking/)
    - [Python Type Hints](https://docs.python.org/3/library/typing.html)
