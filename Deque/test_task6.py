import unittest
from task6 import *


class TestDeque(unittest.TestCase):

    def test_add_front(self):
        deq = Deque()
        deq.addFront(1)
        self.assertEqual(deq.deque, [1])
        self.assertEqual(deq.size(), 1)
        deq.addFront(2)
        self.assertEqual(deq.deque, [2, 1])
        self.assertEqual(deq.size(), 2)

    def test_add_tail(self):
        deq = Deque()
        deq.addFront(1)
        deq.addTail(3)
        self.assertEqual(deq.deque, [1, 3])
        self.assertEqual(deq.size(), 2)
        deq.addTail(4)
        self.assertEqual(deq.deque, [1, 3, 4])
        self.assertEqual(deq.size(), 3)

    def test_remove_front(self):
        deq = Deque()
        deq.addFront(1)
        deq.addFront(22)
        deq.addFront(3)
        self.assertEqual(deq.removeFront(), 3)
        self.assertEqual(deq.removeFront(), 22)
        self.assertEqual(deq.size(), 1)
        self.assertEqual(deq.removeFront(), 1)
        self.assertIsNone(deq.removeFront())

    def test_remove_tail(self):
        deq = Deque()
        deq.addTail(3)
        deq.addTail(4)
        self.assertEqual(deq.removeTail(), 4)
        self.assertEqual(deq.removeTail(), 3)
        self.assertEqual(deq.size(), 0)
        self.assertIsNone(deq.removeTail())


if __name__ == '__main__':
    unittest.main()
