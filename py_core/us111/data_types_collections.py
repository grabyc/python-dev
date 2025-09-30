def list_operations(numbers, to_append=None, to_remove=None):
    result = numbers.copy()
    if to_append is not None:
        result.append(to_append)
    if to_remove in result:
        result.remove(to_remove)
    iteration = [x for x in result]
    return {
        "final_list": result,
        "iteration": iteration
    }

def dict_access(d, key):
    value = d.get(key, "Key not found")
    return {"value": value}

def tuple_immutability(t, index, new_value):
    try:
        t[index] = new_value
    except TypeError as e:
        return {"error": str(e)}
    return {"error": "No error (unexpected)"}

def set_uniqueness(values):
    s = set(values)
    return {"unique_values": list(s)}
