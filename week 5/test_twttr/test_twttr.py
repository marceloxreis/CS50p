from twttr import shorten

def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("Python") == "Pythn"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("CS50") == "CS50"
    assert shorten("I have 2 cats.") == " hv 2 cts."
    assert shorten("AEIOUaeiou") == ""
    assert shorten("") == "" 
    print("All tests passed!")

if __name__ == "__main__":
    test_shorten()
    main()
