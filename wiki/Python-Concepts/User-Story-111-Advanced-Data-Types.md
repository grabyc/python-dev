# User Story 111: Python Advanced Data Types

## Overview
This user story demonstrates the use of Python's advanced built-in data types: lists, dictionaries, tuples, and sets. Understanding these collections is essential for effective data manipulation and organization in Python.

## List Operations
Lists are mutable sequences that can store elements of any type. You can append, remove, and iterate through lists.

**Example:**
```python
numbers = [1, 2, 3]
numbers.append(4)      # [1, 2, 3, 4]
numbers.remove(2)      # [1, 3, 4]
for n in numbers:
    print(n)           # 1 3 4
```

## Dictionary Key-Value Pairs
Dictionaries store key-value pairs and allow fast access to values by key.

**Example:**
```python
d = {"a": 1, "b": 2}
value = d["a"]         # 1
value = d.get("c", "Key not found")  # 'Key not found'
```

## Tuple Immutability
Tuples are immutable sequences. Attempting to modify a tuple raises a TypeError.

**Example:**
```python
t = (1, 2, 3)
# t[1] = 99  # Raises TypeError: 'tuple' object does not support item assignment
```

## Set Uniqueness
Sets are unordered collections of unique elements. Duplicates are automatically removed.

**Example:**
```python
values = [1, 2, 2, 3, 3, 3]
s = set(values)         # {1, 2, 3}
```

## Summary
- Lists are mutable and support dynamic operations.
- Dictionaries provide fast key-based access.
- Tuples are immutable and protect data from modification.
- Sets ensure all elements are unique.

---
For more details, see 
 - the user story in [User Story 111: [Data Types] Learning Advanced Data Types](https://dev.azure.com/gabriel-raby/Python/_workitems/edit/111)
 - the implementation in `data_types_collections.py` and `gradio_app.py` 
 - data types documentation in 
    - [RealPython List Data Type](https://realpython.com/python-list/)
    - [RealPython Tuple Data Type](https://realpython.com/python-tuple/#using-alternatives-to-the-built-in-tuple-type)
    - [RealPython Dictionary Data Type](https://realpython.com/python-dicts/)
    - [RealPython Set Data Type](https://realpython.com/python-sets/)
    - [Python's Built-in Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
