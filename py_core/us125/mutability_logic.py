def modify_list(lst, to_append):
    lst.append(to_append)
    return lst

def modify_tuple(tpl, index, value):
    try:
        tpl[index] = value
    except TypeError as e:
        return str(e), id(tpl)
    return tpl, id(tpl)

def shared_reference_side_effects():
    a = [10, 20]
    b = a
    b.append(30)
    return a, b
