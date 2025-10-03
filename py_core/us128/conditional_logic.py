def simple_if_else(x: int) -> str:
    if x > 5:
        return "x is greater than 5"
    else:
        return "x is not greater than 5"

def multiple_conditions(score: int) -> str:
    if score > 90:
        return "Excellent"
    elif score > 70:
        return "Pass"
    else:
        return "Fail"
