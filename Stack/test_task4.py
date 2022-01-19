import unittest
from task4_stack_tail import *


class TestStack(unittest.TestCase):

    def setUp(self):
        self.Stack = Stack()
        self.Stack.push(4)
        self.Stack.push('dog')
        self.Stack.push(True)
        self.Stack.push('cat')
        self.Stack.push(205)

    def test_stack_push(self):
        self.assertEqual(self.Stack.size(), 5)
        self.Stack.push('stack')
        self.assertEqual(6, self.Stack.size())

    def test_stack_pop(self):
        self.assertEqual(self.Stack.pop(), 205)
        self.assertEqual(self.Stack.pop(), 'cat')
        self.assertEqual(self.Stack.pop(), True)
        self.assertEqual(self.Stack.pop(), 'dog')
        self.assertEqual(self.Stack.pop(), 4)
        self.assertEqual(self.Stack.pop(), None)
        self.assertEqual(self.Stack.pop(), None)
        self.assertEqual(0, self.Stack.size())

    def test_stack_peek(self):
        self.assertEqual(5, self.Stack.size())

        self.Stack.pop()
        self.assertEqual(4, self.Stack.size())

        self.Stack.pop()
        self.assertEqual(3, self.Stack.size())

        self.Stack.push(20)
        self.Stack.push(215)
        self.assertEqual(5, self.Stack.size())
        self.Stack.pop()
        self.Stack.pop()
        self.Stack.pop()
        self.Stack.pop()
        self.Stack.pop()
        self.Stack.pop()
        self.assertEqual(0, self.Stack.size())


if __name__ == '__main__':
    unittest.main()
