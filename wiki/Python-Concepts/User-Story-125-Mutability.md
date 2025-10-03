# User Story 125: Python Mutability

## Overview
This user story demonstrates the concept of mutability in Python, focusing on the behavior of mutable and immutable types, and the effects of shared references.

## Modifying a List (Mutable)
Lists in Python are mutable, meaning their contents can be changed after creation.

**Example:**
```python
lst = [1, 2, 3]
lst.append(4)  # lst is now [1, 2, 3, 4]
```

## Attempting to Modify a Tuple (Immutable)
Tuples are immutable, so their contents cannot be changed after creation. Attempting to do so raises a `TypeError`.

**Example:**
```python
tpl = (1, 2, 3)
tpl[0] = 9  # Raises TypeError: 'tuple' object does not support item assignment
```

## Shared Reference Side Effects
When two variables reference the same mutable object, changes through one variable affect the other.

**Example:**
```python
a = [10, 20]
b = a
b.append(30)
# Now both a and b are [10, 20, 30]
```

## Summary
- Lists are mutable and can be changed in place.
- Tuples are immutable and cannot be changed after creation.
- Shared references to mutable objects can lead to side effects.

---
For more details, see 
 - the user story in [User Story 125: [Data Types] Learn the Difference Between Mutable and Immutable Data Types](https://dev.azure.com/gabriel-raby/Python/_workitems/edit/125)
 - the implementation in `mutability_logic.py` and `gradio_app.py` 
 - type hints documentation in 
    - [RealPython Mutable vs Immutable Types](https://realpython.com/python-mutable-vs-immutable-types/)
