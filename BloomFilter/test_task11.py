import unittest
from task11 import *


class TestBloomFilter(unittest.TestCase):
    def test_all_elements_into_filter(self):
        bf = BloomFilter(32)
        test_arr = ['0123456789', '1234567890', '2345678901', '3456789012', '4567890123', '5678901234',
                    '6789012345', '7890123456', '8901234567', '9012345678']
        for element in test_arr:
            bf.add(element)

        self.assertTrue(bf.is_value('0123456789'))
        self.assertTrue(bf.is_value('4567890123'))
        self.assertTrue(bf.is_value('9012345678'))


if __name__ == '__main__':
    unittest.main()
