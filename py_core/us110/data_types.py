def integer_operations(a: int, b: int):
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b if b != 0 else "Division by zero"
    }

def string_operations(s: str):
    return {
        "concatenation": s + s,
        "slicing (first 3 chars)": s[:3]
    }

def boolean_evaluation(a: int, b: int):
    return {
        "a == b": a == b,
        "a > b": a > b,
        "a < b": a < b
    }
