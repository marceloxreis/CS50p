from bank import value

def test_shorten():
    assert value("hello") == 0
    assert value("H") == 20 # break the code because i use case-insensitivity in the input but need for the task 
    assert value("habib") == 20
    assert value("tetinha") == 100
    assert value("") == 100
    assert value("i have 2 cats.") == 100
    assert value("aeiou") == 100
    assert value("") == 100
    print("All tests passed!")

if __name__ == "__main__":
    test_greeting()
    main()
