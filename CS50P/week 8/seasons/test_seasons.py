import pytest
from datetime import date
from seasons import calculate_minutes_lived, convert_to_words 

def test_calculate_minutes_lived():
    assert calculate_minutes_lived(date(2000, 1, 1)) == (date.today() - date(2000, 1, 1)).days * 24 * 60
    assert calculate_minutes_lived(date(1995, 6, 15)) == (date.today() - date(1995, 6, 15)).days * 24 * 60

def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert convert_to_words(1000000) == "One million"
    assert convert_to_words(1440) == "One thousand, four hundred forty"

if __name__ == "__main__":
    pytest.main()
