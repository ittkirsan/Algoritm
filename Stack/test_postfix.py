import unittest
from task4_postfix import *


class TestPostfix(unittest.TestCase):

    def test_postfix_eval(self):
        self.assertEqual(postfix("8 2 + 5 * 9 + ="), 59)
        self.assertEqual(postfix("8 2 + 5 * k 9 + ="), 59)
        self.assertEqual(postfix("8 2 + 5 * 9 +"), 59)
        self.assertEqual(postfix("82+5*9+="), 59)
        self.assertEqual(postfix("1 2 3 4 5 ="), '5')
        self.assertEqual(postfix("1 2 3 4 5 6 7 8 ="), '8')
        self.assertEqual(postfix("1 2 3 4 5 6 7 8 "), '8')
        self.assertEqual(postfix("1 2 3 4 + + + ="), 10)
        self.assertEqual(postfix("1 2 3 * *  ="), 6)
        self.assertEqual(postfix("1 2 + 3 *  ="), 9)


if __name__ == '__main__':
    unittest.main()
