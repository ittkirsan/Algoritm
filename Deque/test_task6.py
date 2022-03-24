import unittest
from task6 import *


class TestDeque(unittest.TestCase):

    def test_add_front(self):
        deq = Deque()
        deq.add_item_in_head(1)
        self.assertEqual(deq.deque, [1])
        self.assertEqual(deq.len_deque(), 1)
        deq.add_item_in_head(2)
        self.assertEqual(deq.deque, [2, 1])
        self.assertEqual(deq.len_deque(), 2)

    def test_add_tail(self):
        deq = Deque()
        deq.add_item_in_head(1)
        deq.add_item_in_tail(3)
        self.assertEqual(deq.deque, [1, 3])
        self.assertEqual(deq.len_deque(), 2)
        deq.add_item_in_tail(4)
        self.assertEqual(deq.deque, [1, 3, 4])
        self.assertEqual(deq.len_deque(), 3)

    def test_remove_front(self):
        deq = Deque()
        deq.add_item_in_head(1)
        deq.add_item_in_head(22)
        deq.add_item_in_head(3)
        self.assertEqual(deq.delete_head(), 3)
        self.assertEqual(deq.delete_head(), 22)
        self.assertEqual(deq.len_deque(), 1)
        self.assertEqual(deq.delete_head(), 1)
        self.assertIsNone(deq.delete_head())

    def test_remove_tail(self):
        deq = Deque()
        deq.add_item_in_tail(3)
        deq.add_item_in_tail(4)
        self.assertEqual(deq.removeTail(), 4)
        self.assertEqual(deq.removeTail(), 3)
        self.assertEqual(deq.len_deque(), 0)
        self.assertIsNone(deq.removeTail())


if __name__ == '__main__':
    unittest.main()
