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
        OL.add_new_node_by_value(11)
        self.assertEqual(OL.get_all()[0]._value, 11)
        OL.add_new_node_by_value(22)
        self.assertEqual(OL.len(), 2)
        OL.add_new_node_by_value(33)
        OL.add_new_node_by_value(44)
        OL.add_new_node_by_value(55)
        self.assertEqual(OL.len(), 5)
        self.assertEqual(OL.head._value, 11)
        self.assertEqual(OL.tail._value, 55)

    def test_add_descending(self):
        OL = OrderedList(asc=False)
        OL.add_new_node_by_value(10)
        OL.add_new_node_by_value(2)
        OL.add_new_node_by_value(5)
        OL.add_new_node_by_value(8)
        OL.add_new_node_by_value(6)
        self.assertEqual(OL.len(), 5)
        self.assertEqual(OL.head._value, 10)
        self.assertEqual(OL.tail._value, 2)
        self.assertEqual(OL.head.next._value, 8)
        self.assertEqual(OL.head.next.next._value, 6)

    def test_delete(self):
        OL = OrderedList(asc=True)

        OL.add_new_node_by_value(1)
        OL.add_new_node_by_value(2)
        OL.add_new_node_by_value(3)
        OL.add_new_node_by_value(4)
        OL.add_new_node_by_value(5)

        OL.delete_node_value(1)
        self.assertEqual(OL.head._value, 2)

        OL.delete_node_value(5)
        self.assertEqual(OL.tail._value, 4)

        OL.delete_node_value(3)
        self.assertEqual(OL.head._value, 2)
        self.assertEqual(OL.tail._value, 4)
        self.assertEqual(OL.len(), 2)

        OL.delete_node_value(4)
        self.assertEqual(OL.head._value, 2)
        self.assertEqual(OL.tail._value, 2)

    def test_find_asc_true(self):
        OL = OrderedList(asc=True)
        for i in range(30):
            OL.add_new_node_by_value(i)
        self.assertIsNone(OL.find_node_value(100))
        self.assertIsNone(OL.find_node_value(35))
        for i in range(10):
            self.assertEqual(OL.find_node_value(i)._value, i)

    def test_find_descending(self):
        OL = OrderedList(asc=False)
        for i in range(10):
            OL.add_new_node_by_value(i)
        self.assertIsNone(OL.find_node_value(100))
        self.assertIsNone(OL.find_node_value(35))
        for i in range(OL.len()-1, 0):
            self.assertEqual(OL.find_node_value(i).value, i)


class TestOrderedStringList(unittest.TestCase):

    def test_compare(self):
        OSL = OrderedStringList(asc=True)
        self.assertEqual(OSL.compare("string", "    string  "), 0)
        self.assertEqual(OSL.compare("  tex", "    text    "), -1)
        self.assertEqual(OSL.compare("1234", "    12345    "), -1)
        self.assertEqual(OSL.compare("ab", "     "), 1)

    def test_orderd_string_list(self):
        OSL = OrderedStringList(asc=True)
        OSL.add_new_node_by_value("123")
        OSL.add_new_node_by_value("   text")
        OSL.add_new_node_by_value("  aaa  ")
        OSL.add_new_node_by_value("bbbb")
        self.assertEqual(OSL.len(), 4)
        self.assertEqual(OSL.head._value, "123")
        self.assertEqual(OSL.find_node_value("bbb"), None)
        self.assertEqual(OSL.find_node_value("bbbb")._value, "bbbb")

        OSL.delete_node_value("text")
        self.assertEqual(OSL.len(), 3)


if __name__ == '__main__':
    unittest.main()
