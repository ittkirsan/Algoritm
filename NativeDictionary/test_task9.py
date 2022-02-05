import unittest
from task9 import *


class TestNativeDictionary(unittest.TestCase):
    def setUp(self):

        self.ND = NativeDictionary(20)
        self.ND.put('ключ', 'text')
        self.ND.put('ключ1', 123)
        self.ND.put('ключ2', 456)
        self.ND.put('ключ3', 'book')
        self.ND.put('ключ4', 789)
        self.ND.put('ключ5', 'string')

    def test_put(self):
        self.ND.put('aaaa', 4587)
        self.assertEqual(4587, self.ND.get('aaaa'))
        self.assertEqual('text', self.ND.get('ключ'))

        self.ND.put('ключ', 42365)
        self.assertEqual(42365, self.ND.get('ключ'))
        self.assertEqual('string', self.ND.get('ключ5'))

        self.ND.put('ключ5', 'string_and_text')
        self.assertEqual('string_and_text', self.ND.get('ключ5'))

        self.assertIsNone(self.ND.put(111111, 256))
        self.assertIsNone(self.ND.put(111111, 'text'))

    def test_is_key(self):
        self.assertIsNone(self.ND.is_key(111111))
        self.assertEqual(True, self.ND.is_key('ключ'))
        self.assertEqual(True, self.ND.is_key('ключ2'))
        self.assertEqual(True, self.ND.is_key('ключ5'))
        self.assertEqual(False, self.ND.is_key('text'))
        self.assertEqual(False, self.ND.is_key('кл'))

    def test_get(self):
        self.assertEqual('text', self.ND.get('ключ'))
        self.assertEqual('string', self.ND.get('ключ5'))
        self.assertEqual(123, self.ND.get('ключ1'))
        self.assertEqual(None, self.ND.get('key'))
        self.assertEqual(None, self.ND.get('key2'))
        self.assertEqual(None, self.ND.get('key5'))
        self.assertEqual(None, self.ND.get(1233))


if __name__ == '__main__':
    unittest.main()
