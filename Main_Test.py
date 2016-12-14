import unittest

from main import *


class Test(unittest.TestCase):
    def test_1(self):
        expected = "Lviv"
        actual = main("Lviv")
        self.assertEqual(expected, actual, "Error")

    def test_2(self):
        expected = "Hi!"
        actual = main("Hi!")
        self.assertEqual(expected, actual, "Error")

    def test_3(self):
        expected = "_DrEaM123_"
        actual = main("_DrEaM123_")
        self.assertEqual(expected, actual, "Error")

    def test_4(self):
        expected = "1234567890"
        actual = main("1234567890")
        self.assertEqual(expected, actual, "Error")

    def test_5(self):
        expected = "0a1b2c"
        actual = main("0a1b2c")
        self.assertEqual(expected, actual, "Error")

    def test_6(self):
        expected = "zxcvbnm,./"
        actual = main("zxcvbnm,./")
        self.assertEqual(expected, actual, "Error")

    def test_7(self):
        expected = "-7-5-4 %^& @3"
        actual = main("-7-5-4 %^& @3")
        self.assertEqual(expected, actual, "Error")

    def test_8(self):
        expected = "~~~~~~~~~~"
        actual = main("~~~~~~~~~~")
        self.assertEqual(expected, actual, "Error")

    def test_9(self):
        expected = "H     j"
        actual = main("H     j")
        self.assertEqual(expected, actual, "Error")

    def test_10(self):
        expected = "                   "
        actual = main("                   ")
        self.assertEqual(expected, actual, "Error")