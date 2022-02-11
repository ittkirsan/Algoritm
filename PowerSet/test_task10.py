
import unittest
from task10 import *


class TestPowerSe(unittest.TestCase):

    def test_size(self):
        ps = PowerSet()
        self.assertEqual(ps.size(), 0)
        ps.put("text")
        self.assertEqual(ps.size(), 1)
        ps.put("text")
        self.assertEqual(ps.size(), 1)
        ps.put("123")
        self.assertEqual(ps.size(), 2)

    def test_put(self):
        ps = PowerSet()
        self.assertEqual(ps.size(), 0)
        ps.put("1")
        self.assertEqual(ps.size(), 1)
        ps.put("1")
        self.assertEqual(ps.size(), 1)
        ps.put("123")
        self.assertEqual(ps.size(), 2)
        ps.put("123")
        self.assertEqual(ps.size(), 2)

    def test_remove(self):
        ps = PowerSet()
        self.assertFalse(ps.remove("123"))
        ps.put("123")
        self.assertEqual(ps.size(), 1)
        self.assertTrue(ps.remove("123"))
        self.assertEqual(ps.size(), 0)
        self.assertFalse(ps.remove("222"))
        self.assertEqual(ps.size(), 0)
        ps.put("1")
        ps.put("1")
        self.assertEqual(ps.size(), 1)
        self.assertTrue(ps.remove("1"))
        self.assertFalse(ps.remove("1"))
        self.assertFalse(ps.get("123"))
        self.assertFalse(ps.get("1"))
        self.assertEqual(ps.size(), 0)

    def test_intersection(self):
        set1 = PowerSet()
        set1.put("1")
        set1.put("2")
        set1.put("3")

        set2 = PowerSet()
        set2.put("4")
        set2.put("5")
        set2.put("6")

        set3 = set1.intersection(set2)
        self.assertEqual(set3.size(), 0)

        set1.put("4")
        set2.put("3")
        set4 = set1.intersection(set2)
        self.assertEqual(set4.size(), 2)
        self.assertTrue(set4.get("3"))
        self.assertTrue(set4.get("4"))

    def test_union(self):
        set1 = PowerSet()
        set2 = PowerSet()

        set3 = set1.union(set2)
        self.assertEqual(set3.size(), 0)

        set1.put("1")
        set1.put("2")
        set1.put("3")
        set2.put("3")
        set2.put("4")
        set2.put("5")
        set4 = set1.union(set2)
        self.assertEqual(set4.size(), 5)
        self.assertTrue(set4.get("1"))
        self.assertTrue(set4.get("2"))
        self.assertTrue(set4.get("3"))
        self.assertTrue(set4.get("4"))
        self.assertTrue(set4.get("5"))

    def test_difference(self):
        set1 = PowerSet()
        set2 = PowerSet()
        set3 = set1.difference(set2)
        self.assertEqual(set3.size(), 0)

        set1.put("1")
        set1.put("2")
        set1.put("3")
        set4 = set1.difference(set2)
        self.assertEqual(set4.size(), 3)

        set2.put("1")
        set2.put("2")
        set5 = set1.difference(set2)
        self.assertEqual(set5.size(), 1)
        self.assertFalse(set5.get("1"))
        self.assertFalse(set5.get("2"))
        self.assertTrue(set5.get("3"))

        set2.put("3")
        set6 = set1.difference(set2)
        self.assertEqual(set6.size(), 0)

    def test_issubset(self):
        set1 = PowerSet()
        set2 = PowerSet()
        self.assertTrue(set1.issubset(set2))

        set1.put("1")
        set1.put("2")
        set1.put("3")
        self.assertTrue(set1.issubset(set2))

        set2.put("4")
        set2.put("5")
        set2.put("6")
        self.assertFalse(set1.issubset(set2))

        set3 = PowerSet()
        set3.put("2")
        set3.put("3")
        self.assertTrue(set1.issubset(set3))

    def test_hiload(self):
        set1, set2 = PowerSet(), PowerSet()
        for i in range(20000):
            set1.put(str(i))

        for i in range(200):
            set2.put(str(i))

        self.assertEqual(set1.size(), 20000)
        self.assertEqual(set2.size(), 200)


if __name__ == '__main__':
    unittest.main()
