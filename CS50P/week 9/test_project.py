import pytest
import re
from project import function_length, function_symbols, function_str

def test_function_length(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "8")
    assert function_length() == 8

    monkeypatch.setattr("builtins.input", lambda _: "15")
    assert function_length() == 15

def test_function_symbols(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert function_symbols() == True

    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert function_symbols() == False

def test_function_str():
    password = function_str(10, True)  # Generate password with symbols
    assert len(password) == 10  # Ensure correct length
    assert re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    password_no_symbols = function_str(10, False)  # Generate password without symbols
    assert len(password_no_symbols) == 10  # Ensure correct length
    assert all(char.isalnum() for char in password_no_symbols)  # Ensure only letters/numbers

if __name__ == "__main__":
    pytest.main()
