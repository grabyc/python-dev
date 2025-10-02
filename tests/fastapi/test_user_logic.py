from py_fastapi.us66.user_logic import User, process_user
import pytest
from pydantic import ValidationError

def test_process_user_valid():
    user = User(name="Alice", email="alice@example.com")
    result = process_user(user)
    assert result == {"name": "Alice", "email": "alice@example.com"}

def test_process_user_invalid_email():
    with pytest.raises(ValidationError):
        User(name="Alice", email="not-an-email")

def test_process_user_missing_name():
    with pytest.raises(ValidationError):
        User(email="alice@example.com")
