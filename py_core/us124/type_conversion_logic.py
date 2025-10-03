def implicit_conversion(a: int, b: float) -> float:
    return a + b

def explicit_conversion(num_str: str) -> int:
    return int(num_str)

def conversion_error(invalid_str: str):
    try:
        return int(invalid_str)
    except ValueError as e:
        return str(e)
