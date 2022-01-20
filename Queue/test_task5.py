import unittest
from task5 import *


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue('queue')
        self.queue.enqueue(1)
        self.queue.enqueue('2')
        self.queue.enqueue(3)

    def test_queue_push(self):
        self.assertEqual(self.queue.size(), 4)
        self.queue.enqueue('5')
        self.queue.enqueue(202)
        self.queue.enqueue('7')
        self.queue.enqueue('8')
        self.assertEqual(8, self.queue.size())

    def test_queue_pop(self):
        self.queue.enqueue('5')
        self.queue.enqueue(202)
        self.queue.enqueue('7')
        self.queue.enqueue('8')
        self.assertEqual(self.queue.dequeue(), 'queue')
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), '2')
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(4, self.queue.size())
        self.assertEqual(self.queue.dequeue(), '5')
        self.assertEqual(self.queue.dequeue(), 202)
        self.assertEqual(self.queue.dequeue(), '7')
        self.assertEqual(1, self.queue.size())


if __name__ == '__main__':
    unittest.main()
