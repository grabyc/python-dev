"""
Module: looping_logic.py
Contains functions for demonstrating for and while loop logic for testing and Gradio UI.
"""

def for_loop_elements(lst):
    """Returns a list of elements as they would be printed in a for loop."""
    output = []
    for elem in lst:
        output.append(str(elem))
    return output

def while_loop_counter(x):
    """Returns a list of counter values as they would be printed in a while loop incrementing x until x < 3."""
    output = []
    while x < 3:
        output.append(str(x))
        x += 1
    return output
