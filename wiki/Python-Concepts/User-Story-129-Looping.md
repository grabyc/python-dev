# User Story 129: Python Looping (For and While)

## Overview
This user story demonstrates the use of looping statements in Python, specifically the `for` and `while` loops. Looping allows you to repeat actions efficiently and process sequences of data.

## Purpose
- Show how to use `for` loops to iterate over sequences
- Show how to use `while` loops to repeat actions based on a condition
- Provide practical examples for both loop types

## Examples
### For Loop Example
```python
lst = [1, 2, 3]
for elem in lst:
    print(elem)
# Output:
# 1
# 2
# 3
```

### While Loop Example
```python
x = 0
while x < 3:
    print(x)
    x += 1
# Output:
# 0
# 1
# 2
```

## Key Points
- `for` loops are ideal for iterating over known sequences (lists, tuples, strings, etc.).
- `while` loops are useful when the number of iterations is not known in advance and depends on a condition.

---
For more details, see 
 - the user story in [User Story 129: [Control Flow] Loops (for and while)](https://dev.azure.com/gabriel-raby/Python/_workitems/edit/129)
 - the implementation in `looping_logic.py` and `gradio_app.py` 
 - Looping documentation at 
    - [Python Documentation: for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
    - [Python Documentation: while Statements](https://docs.python.org/3/tutorial/controlflow.html#the-while-statement)
    - [Real Python: For Loops](https://realpython.com/python-for-loop/)
    - [Real Python: While Loops](https://realpython.com/python-while-loop/)
