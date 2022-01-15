import unittest
from task3 import *


class TestDynarray(unittest.TestCase):
    def setUp(self):
        self.Dynarray_10_eltments = DynArray()
        self.Dynarray_16_eltments = DynArray()
        for i in range(10):
            self.Dynarray_10_eltments.append(i)
        for i in range(16):
            self.Dynarray_16_eltments.append(i)

    def test_insert_buffer_not_exceed(self):
        self.assertEqual(self.Dynarray_10_eltments.capacity, 16)
        self.assertEqual(self.Dynarray_16_eltments.capacity, 16)

        self.Dynarray_10_eltments.insert(5, 202)
        self.assertEqual(self.Dynarray_10_eltments[6], 5)
        self.assertEqual(self.Dynarray_10_eltments.capacity, 16)
        self.assertEqual(self.Dynarray_10_eltments.count, 11)

    def test_insert_buffer_exceed(self):
        self.assertEqual(self.Dynarray_10_eltments.capacity, 16)
        self.assertEqual(self.Dynarray_16_eltments.capacity, 16)

        self.Dynarray_16_eltments.insert(5, 202)
        self.assertEqual(self.Dynarray_16_eltments[6], 5)
        self.assertEqual(self.Dynarray_16_eltments[5], 202)
        self.assertEqual(self.Dynarray_16_eltments.capacity, 32)
        self.assertEqual(self.Dynarray_16_eltments.count, 17)

    def test_delete_10(self):
        self.assertEqual(self.Dynarray_10_eltments.capacity, 16)

        self.Dynarray_10_eltments.delete(5)
        self.assertEqual(self.Dynarray_10_eltments[5], 6)
        self.assertEqual(self.Dynarray_10_eltments.capacity, 16)
        self.assertEqual(self.Dynarray_10_eltments.count, 9)

        self.Dynarray_10_eltments.delete(5)
        self.assertEqual(self.Dynarray_10_eltments[5], 7)
        self.assertEqual(self.Dynarray_10_eltments.capacity, 16)
        self.assertEqual(self.Dynarray_10_eltments.count, 8)

        self.Dynarray_10_eltments.delete(5)
        self.assertEqual(self.Dynarray_10_eltments[5], 8)
        self.assertEqual(self.Dynarray_10_eltments.capacity, 16)
        self.assertEqual(self.Dynarray_10_eltments.count, 7)

        with self.assertRaises(IndexError):
            self.Dynarray_10_eltments.delete(30)

    def test_delete_16(self):
        self.assertEqual(self.Dynarray_16_eltments.capacity, 16)

        self.Dynarray_16_eltments.insert(5, 101)
        self.assertEqual(self.Dynarray_16_eltments[6], 5)
        self.assertEqual(self.Dynarray_16_eltments.capacity, 32)
        self.assertEqual(self.Dynarray_16_eltments.count, 17)

        self.Dynarray_16_eltments.delete(4)
        self.Dynarray_16_eltments.delete(10)
        self.assertEqual(self.Dynarray_16_eltments[4], 101)
        self.assertEqual(self.Dynarray_16_eltments.capacity, 21)
        self.assertEqual(self.Dynarray_16_eltments.count, 15)

        with self.assertRaises(IndexError):
            self.Dynarray_10_eltments.delete(100)


if __name__ == '__main__':
    unittest.main()
