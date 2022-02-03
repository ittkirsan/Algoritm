import unittest
from task8 import *


class TestHashTable(unittest.TestCase):
    def setUp(self):
        size = 17
        step = 3
        self.ht = HashTable(size, step)
        self.values = ["string123", "string",
                       "gnirts", "string1", "string2", "string6"]

    def test_hash_fun(self):

        self.assertEqual(14, self.ht.hash_fun("string123"))
        self.assertEqual(14, self.ht.hash_fun("string231"))  # коллизия
        self.assertEqual(0, self.ht.hash_fun("string"))
        self.assertEqual(3, self.ht.hash_fun("string6"))
        self.assertIsNone(self.ht.hash_fun(11111))

    def test_seek_slot(self):

        index = self.ht.seek_slot(self.values[0])
        self.assertEqual(14, index)
        index = self.ht.seek_slot(self.values[1])
        self.assertEqual(0, index)
        index = self.ht.seek_slot(self.values[2])
        self.assertEqual(0, index)
        index = self.ht.seek_slot(self.values[3])
        self.assertEqual(15, index)
        index = self.ht.seek_slot(self.values[4])
        self.assertEqual(16, index)
        self.assertEqual(0, self.ht.seek_slot("gnirts"))
        index = self.ht.seek_slot(11111)
        self.assertIsNone(index)

    def test_put(self):

        self.assertEqual(14,  self.ht.put(self.values[0]))
        self.assertEqual(0, self.ht.put(self.values[1]))
        # коллизия. ищем свободный слот
        self.assertEqual(3, self.ht.put(self.values[2]))
        self.assertEqual(15, self.ht.put(self.values[3]))
        self.assertEqual(16, self.ht.put(self.values[4]))
        self.assertEqual(6, self.ht.put(self.values[5]))
        self.assertEqual(9, self.ht.put('6string'))

    def test_find(self):
        for v in self.values:
            self.ht.put(v)

        self.assertEqual(14, self.ht.find(self.values[0]))
        self.assertEqual(0, self.ht.find(self.values[1]))
        self.assertEqual(3, self.ht.find(self.values[2]))

        self.assertIsNone(self.ht.find(111111))


if __name__ == '__main__':
    unittest.main()
