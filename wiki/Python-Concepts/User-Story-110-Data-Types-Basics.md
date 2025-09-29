# User Story 110: Python Data Types Basics

## Overview
This user story demonstrates the use of Python's built-in data types, focusing on their basic operations and behaviors. Understanding these types is fundamental to writing effective Python code.

## Integer Operations
Python supports arithmetic operations on integers, such as addition, subtraction, multiplication, and division.

**Example:**
```python
a = 7
b = 3
addition = a + b        # 10
subtraction = a - b     # 4
multiplication = a * b  # 21
division = a / b        # 2.333...
```

## String Operations
Strings in Python can be concatenated and sliced to create new strings or extract substrings.

**Example:**
```python
s = "hello"
concatenation = s + s   # 'hellohello'
slice = s[:3]           # 'hel'
```

## Boolean Evaluation
Python evaluates expressions and comparisons to boolean values (`True` or `False`).

**Example:**
```python
a = 5
b = 3
is_equal = a == b       # False
is_greater = a > b      # True
is_less = a < b         # False
```

## Summary
- Integers support standard arithmetic operations.
- Strings can be concatenated and sliced.
- Boolean expressions evaluate to `True` or `False` based on the logic.

---
For more details, see 
 - the user story in [User Story 110: [Data Types] Understanding Basic Data Types](https://dev.azure.com/gabriel-raby/Python/_workitems/edit/110)
 - the implementation in `data_types.py` and `gradio_app.py` 
 - data types documentation in 
    - [RealPython Data Types](https://realpython.com/python-data-types/)
    - [Python's Built-in Types](https://docs.python.org/3/library/stdtypes.html)

