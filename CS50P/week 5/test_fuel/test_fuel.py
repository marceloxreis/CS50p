import unittest
from fuel import convert, gauge

class TestFuelFunctions(unittest.TestCase):
    def test_convert_valid(self):
        self.assertEqual(convert("3/4"), 75)
        self.assertEqual(convert("1/4"), 25)
        self.assertEqual(convert("1/100"), 1)
        self.assertEqual(convert("100/100"), 100)
        self.assertEqual(convert("0/100"), 0)

    def test_convert_invalid(self):
        with self.assertRaises(ValueError):
            convert("4/3")
        with self.assertRaises(ValueError):
            convert("abc/def")
        with self.assertRaises(ValueError):
            convert("1.5/2.5")
        with self.assertRaises(ZeroDivisionError):
            convert("1/0")
        with self.assertRaises(ValueError):
            convert("1/")
        with self.assertRaises(ValueError):
            convert("/1")
        with self.assertRaises(ValueError):
            convert("1")

    def test_gauge(self):
        self.assertEqual(gauge(0), "E")
        self.assertEqual(gauge(1), "E")
        self.assertEqual(gauge(99), "F")
        self.assertEqual(gauge(100), "F")
        self.assertEqual(gauge(50), "50%")
        self.assertEqual(gauge(25), "25%")
        self.assertEqual(gauge(75), "75%")

if __name__ == "__main__":
    unittest.main()
