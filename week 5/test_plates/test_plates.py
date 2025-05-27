from plates import is_valid

def test_is_valid():
    # Valid plates
    assert is_valid("CS50") == True  # Proper format
    assert is_valid("AB1234") == True  # Maximum length, starts with letters
    assert is_valid("XY9") == True  # Single number after letters
    assert is_valid("AAA222") == True  # All conditions met

    # Invalid plates: Length checks
    assert is_valid("A") == False  # Too short
    assert is_valid("ABCDEFG") == False  # Too long
    assert is_valid("123456") == False  # Too long

    # Invalid plates: Non-alphanumeric characters
    assert is_valid("CS50!") == False  # Contains an exclamation mark
    assert is_valid("AB-123") == False  # Contains a hyphen

    # Invalid plates: Starts with non-alphabetic characters
    assert is_valid("1ABC") == False  # Starts with a number
    assert is_valid("!CS50") == False  # Starts with a symbol

    # Invalid plates: Number placement
    assert is_valid("CS50A") == False  # Letters after numbers
    assert is_valid("CS012") == False  # Number starts with zero

    # Invalid plates: Empty string
    assert is_valid("") == False  # Empty input

    print("All tests passed!")

