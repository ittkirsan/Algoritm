import unittest
from task5_4 import *


class TestQueue2(unittest.TestCase):

    def test_queue2(self):
        Qs = Queue2()
        self.assertEqual(Qs.size(), 0)
        Qs.enqueue(111)
        Qs.enqueue(222)
        Qs.enqueue(333)
        self.assertEqual(Qs.size(), 3)
        self.assertEqual(Qs.dequeue(), 111)
        self.assertEqual(Qs.dequeue(), 222)
        self.assertEqual(Qs.size(), 1)


if __name__ == '__main__':
    unittest.main()
