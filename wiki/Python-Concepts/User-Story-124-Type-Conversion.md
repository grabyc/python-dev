# User Story 124: Python Type Conversion and Coercion

## Overview
This user story demonstrates the use of type conversion (type coercion) in Python, including both implicit and explicit conversions, as well as error handling for invalid conversions.

## Implicit Conversion (Type Coercion)
Python automatically converts types in some operations. For example, when adding an integer and a float, the result is a float.

**Example:**
```python
a = 2      # int
b = 3.5    # float
result = a + b  # result is 5.5 (float)
```

## Explicit Conversion
You can explicitly convert values from one type to another using built-in functions like `int()`, `float()`, or `str()`.

**Example:**
```python
num_str = "42"
num = int(num_str)  # num is 42 (int)
```

## Conversion Error Handling
If you try to convert an invalid value, Python raises a `ValueError`.

**Example:**
```python
invalid_str = "abc"
try:
    num = int(invalid_str)
except ValueError as e:
    print(e)  # Output: invalid literal for int() with base 10: 'abc'
```

## Summary
- Python performs implicit type conversion in some operations (e.g., int + float → float).
- Use explicit conversion functions to change types as needed.
- Always handle possible conversion errors when input may be invalid.

---
For more details, see 
 - the user story in [User Story 124: [Data Types] Understand Type Coercion and Conversion in Python](https://dev.azure.com/gabriel-raby/Python/_workitems/edit/124)
 - the implementation in `type_convresion_logic.py` and `gradio_app.py` 
 - type hints documentation in 
    - [Type Conversion](https://llego.dev/posts/python-type-conversion-guide/)

