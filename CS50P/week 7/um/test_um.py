import pytest
from um import count

def test_basic_cases():
    assert count("um") == 1
    assert count("Um Um um") == 3
    assert count("um um um um") == 4
    assert count("This is a test with um inside.") == 1

def test_inside_words():
    assert count("yummy") == 0  # "um" inside a word should not count
    assert count("album") == 0  # "um" inside a word should not count
    assert count("Um, I think um is here.") == 2  # Comma should not break detection

def test_spaces_around():
    assert count(" um ") == 1
    assert count("the um is here") == 1
    assert count("the um's case is important") == 1  # Apostrophe case

def test_case_insensitive():
    assert count("UM Um uM um") == 4  # Should be case insensitive
    assert count("UM in a sentence is still um") == 2

def test_no_um():
    assert count("This sentence has no target word.") == 0
    assert count("Completely unrelated words.") == 0

if __name__ == "__main__":
    pytest.main()
