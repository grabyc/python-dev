from add import add

def test_add():
    assert add(2, 3) == 5

def test_add_fail():
    assert add(2, 3) == 6  # This will fail
