class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0  # Track number of cookies in the jar


    def __str__(self):
        return "🍪" * self._size


    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer.")

        if self._size + n > self._capacity:
            raise ValueError("Capacity exceeded.")

        self._size += n  # Add cookies instead of overwriting


    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer.")

        if   n > self._size:
            raise ValueError("Exceeded the amount.")

        self._size -= n  # Add cookies instead of overwriting


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
