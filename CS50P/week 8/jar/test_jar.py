import pytest
from jar import Jar

def test_init():
    jar = Jar(12)
    assert jar.capacity == 12

    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("13")
def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(4)
    assert jar.size == 9

    with pytest.raises(ValueError):
        jar.deposit(4)

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7

    jar.withdraw(4)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(4)




