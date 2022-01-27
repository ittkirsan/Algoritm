import unittest
from task6_2 import *


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(palindrome(""))
        self.assertTrue(palindrome("Лёша на полке клопа нашёл"))
        self.assertTrue(palindrome("76543211234567"))
        self.assertTrue(palindrome("А роза упала на лапу Азора"))
        self.assertTrue(palindrome("1"))
        self.assertFalse(palindrome("aaAAB"))


if __name__ == '__main__':
    unittest.main()
