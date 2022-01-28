import unittest
from task7 import *


class TestOrderedList(unittest.TestCase):

    def test_compare(self):
        OL = OrderedList(asc=True)
        self.assertEqual(OL.compare(5, 5), 0)
        self.assertEqual(OL.compare(1, 2), -1)
        self.assertEqual(OL.compare(3, 1), 1)

    def test_add(self):
        OL = OrderedList(asc=True)
        OL.add(11)
        self.assertEqual(OL.get_all()[0].value, 11)
        OL.add(22)
        self.assertEqual(OL.len(), 2)
        OL.add(33)
        OL.add(44)
        OL.add(55)
        self.assertEqual(OL.len(), 5)
        self.assertEqual(OL.head.value, 11)
        self.assertEqual(OL.tail.value, 55)

    def test_add_descending(self):
        OL = OrderedList(asc=False)
        OL.add(10)
        OL.add(2)
        OL.add(5)
        OL.add(8)
        OL.add(6)
        self.assertEqual(OL.len(), 5)
        self.assertEqual(OL.head.value, 10)
        self.assertEqual(OL.tail.value, 2)
        self.assertEqual(OL.head.next.value, 8)
        self.assertEqual(OL.head.next.next.value, 6)

    def test_delete(self):
        OL = OrderedList(asc=True)

        OL.add(1)
        OL.add(2)
        OL.add(3)
        OL.add(4)
        OL.add(5)

        OL.delete(1)
        self.assertEqual(OL.head.value, 2)

        OL.delete(5)
        self.assertEqual(OL.tail.value, 4)

        OL.delete(3)
        self.assertEqual(OL.head.value, 2)
        self.assertEqual(OL.tail.value, 4)
        self.assertEqual(OL.len(), 2)

        OL.delete(4)
        self.assertEqual(OL.head.value, 2)
        self.assertEqual(OL.tail.value, 2)

    def test_find_asc_true(self):
        OL = OrderedList(asc=True)
        for i in range(30):
            OL.add(i)
        self.assertIsNone(OL.find(100))
        self.assertIsNone(OL.find(35))
        for i in range(10):
            self.assertEqual(OL.find(i).value, i)

    def test_find_descending(self):
        OL = OrderedList(asc=False)
        for i in range(10):
            OL.add(i)
        self.assertIsNone(OL.find(100))
        self.assertIsNone(OL.find(35))
        for i in range(OL.len()-1, 0):
            self.assertEqual(OL.find(i).value, i)


class TestOrderedStringList(unittest.TestCase):

    def test_compare(self):
        OSL = OrderedStringList(asc=True)
        self.assertEqual(OSL.compare("string", "    string  "), 0)
        self.assertEqual(OSL.compare("  tex", "    text    "), -1)
        self.assertEqual(OSL.compare("1234", "    12345    "), -1)
        self.assertEqual(OSL.compare("ab", "     "), 1)

    def test_orderd_string_list(self):
        OSL = OrderedStringList(asc=True)
        OSL.add("123")
        OSL.add("   text")
        OSL.add("  aaa  ")
        OSL.add("bbbb")
        self.assertEqual(OSL.len(), 4)
        self.assertEqual(OSL.head.value, "123")
        self.assertEqual(OSL.find("bbb"), None)
        self.assertEqual(OSL.find("bbbb").value, "bbbb")

        OSL.delete("text")
        self.assertEqual(OSL.len(), 3)


if __name__ == '__main__':
    unittest.main()
