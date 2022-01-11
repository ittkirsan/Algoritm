'''Tесты для task2_10. Двунаправленный список c фиктивными узлами.'''
import unittest
import random
from task2_10 import *


class TestLinkedListWihtDummyNodes(unittest.TestCase):
    def setUp(self):
        self.empty_LinkedListWihtDummyNodes = LinkedListWihtDummyNodes()

        self.LinkedListWihtDummyNodes_with_one_element = LinkedListWihtDummyNodes()
        self.node = Node(33)
        self.node1_11 = Node(15)
        self.node1_12 = Node(16)
        self.LinkedListWihtDummyNodes_with_one_element.add_in_tail(self.node)

        self.LinkedListWihtDummyNodes_with_10_elements = LinkedListWihtDummyNodes()
        self.node_1 = Node(15)
        self.node_2 = Node(20)
        self.node_3 = Node(25)
        self.node_4 = Node(440)
        self.node_5 = Node(35)
        self.node_6 = Node(45)
        self.node_7 = Node(440)
        self.node_8 = Node(50)
        self.node_9 = Node(440)
        self.node_10 = Node(5)
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_tail(self.node_1)
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_tail(self.node_2)
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_tail(self.node_3)
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_tail(self.node_4)
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_tail(self.node_5)
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_tail(self.node_6)
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_tail(self.node_7)
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_tail(self.node_8)
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_tail(self.node_9)
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_tail(
            self.node_10)

        self.LinkedListWihtDummyNodes_many_elements = LinkedListWihtDummyNodes()
        self.N = random.randint(1, 200)
        for i in range(self.N):
            self.LinkedListWihtDummyNodes_many_elements.add_in_tail(
                Node(random.randint(1, 500)))

    # метод len()

    def test_len_empty_LinkedListWihtDummyNodes(self):
        self.assertEqual(0, self.empty_LinkedListWihtDummyNodes.len())

    def test_len_LinkedListWihtDummyNodes_with_one_element(self):
        self.assertEqual(
            1, self.LinkedListWihtDummyNodes_with_one_element.len())

    def test_len_LinkedListWihtDummyNodes_with_10_elements(self):
        self.assertEqual(
            10, self.LinkedListWihtDummyNodes_with_10_elements.len())

    # метод clean()
    def test_clean_empty_LinkedListWihtDummyNodes(self):
        self.assertEqual(None, self.empty_LinkedListWihtDummyNodes.clean())

    def test_clean_list_with_one_element(self):
        self.assertEqual(
            self.LinkedListWihtDummyNodes_with_one_element.clean(), None)

    def test_clean_LinkedListWihtDummyNodes_with_10_elements(self):
        self.assertEqual(
            self.LinkedListWihtDummyNodes_with_10_elements.clean(), None)

    def test_clean_LinkedListWihtDummyNodes_many_elements(self):
        length = self.LinkedListWihtDummyNodes_many_elements.len()
        self.LinkedListWihtDummyNodes_many_elements.clean()
        self.assertNotEqual(
            length, self.LinkedListWihtDummyNodes_many_elements.len())
        self.assertEqual(0, self.LinkedListWihtDummyNodes_many_elements.len())

   # метод find_all()

    def test_find_all_empty_LinkedListWihtDummyNodes(self):
        self.assertEqual([], self.empty_LinkedListWihtDummyNodes.find_all(10))
        self.assertEqual([], self.empty_LinkedListWihtDummyNodes.find_all(25))
        self.assertEqual(
            [], self.empty_LinkedListWihtDummyNodes.find_all(1564))

    def test_find_all_LinkedListWihtDummyNodes_with_one_element(self):
        self.assertEqual(
            [], self.LinkedListWihtDummyNodes_with_one_element.find_all(155))
        self.assertEqual(
            [self.node], self.LinkedListWihtDummyNodes_with_one_element.find_all(33))

    def test_find_all_LinkedListWihtDummyNodes_with_10_elements(self):
        self.assertEqual([self.node_4, self.node_7, self.node_9],
                         self.LinkedListWihtDummyNodes_with_10_elements.find_all(440))
        self.assertEqual(
            [self.node_3], self.LinkedListWihtDummyNodes_with_10_elements.find_all(25))
        self.assertEqual(
            [], self.LinkedListWihtDummyNodes_with_10_elements.find_all(1567))
        self.assertEqual(
            [], self.LinkedListWihtDummyNodes_with_10_elements.find_all(0))

    # метод delete

    def test_delete_empty_LinkedListWihtDummyNodes_false(self):
        self.empty_LinkedListWihtDummyNodes.delete(15)
        self.assertEqual(0, self.empty_LinkedListWihtDummyNodes.len())

    def test_delete_LinkedListWihtDummyNodes_with_one_element_false(self):
        self.LinkedListWihtDummyNodes_with_one_element.delete(15)
        self.assertEqual(
            self.LinkedListWihtDummyNodes_with_one_element.len(), 1)

        self.LinkedListWihtDummyNodes_with_one_element.delete(33)
        self.assertEqual(
            self.LinkedListWihtDummyNodes_with_one_element.len(), 0)

    def test_delete_LinkedListWihtDummyNodes_with_10_elements_false(self):
        self.LinkedListWihtDummyNodes_with_10_elements.delete(1532)
        self.assertEqual(
            10, self.LinkedListWihtDummyNodes_with_10_elements.len())

        self.LinkedListWihtDummyNodes_with_10_elements.delete(15)
        self.assertEqual(
            self.LinkedListWihtDummyNodes_with_10_elements.len(), 9)

        self.LinkedListWihtDummyNodes_with_10_elements.delete(5)
        self.LinkedListWihtDummyNodes_with_10_elements.delete(440)
        self.assertEqual(self.node_3.next, self.node_5)
        self.assertEqual(self.node_5.prev, self.node_3)
        self.assertEqual(self.node_7.value, 440)
        self.assertEqual(
            self.LinkedListWihtDummyNodes_with_10_elements.len(), 7)

    # удаление всех узлв с заданным значением
    def test_delete_empty_LinkedListWihtDummyNodes_true(self):
        self.empty_LinkedListWihtDummyNodes.delete(10, True)
        self.assertEqual(0, self.empty_LinkedListWihtDummyNodes.len())

    def test_delete_LinkedListWihtDummyNodes_with_one_element_true(self):
        self.LinkedListWihtDummyNodes_with_one_element.delete(33, True)
        self.assertEqual(
            0, self.LinkedListWihtDummyNodes_with_one_element.len())
        self.assertEqual(
            None, self.LinkedListWihtDummyNodes_with_10_elements.find(33))

    def test_delete_LinkedListWihtDummyNodes_with_10_elements_true(self):
        self.LinkedListWihtDummyNodes_with_10_elements.delete(154, True)
        self.assertEqual(
            10, self.LinkedListWihtDummyNodes_with_10_elements.len())
        self.LinkedListWihtDummyNodes_with_10_elements.delete(440, True)
        self.assertEqual(
            7, self.LinkedListWihtDummyNodes_with_10_elements.len())
        self.assertEqual(
            None, self.LinkedListWihtDummyNodes_with_10_elements.find(440))
        self.assertEqual(self.node_8.prev, self.node_6)
        self.assertEqual(self.node_8.next.value, 5)

    # метод insert()

    def test_insert_empty_LinkedListWihtDummyNodes(self):
        self.empty_LinkedListWihtDummyNodes.insert(None, self.node)
        self.assertEqual(1, self.empty_LinkedListWihtDummyNodes.len())

    def test_insert_LinkedListWihtDummyNodes_with_one_element(self):
        self.LinkedListWihtDummyNodes_with_one_element.insert(
            self.node, self.node1_11)
        self.assertEqual(
            2, self.LinkedListWihtDummyNodes_with_one_element.len())
        self.assertEqual(self.node1_11.prev, self.node)
        self.assertEqual(self.node.next, self.node1_11)

        self.LinkedListWihtDummyNodes_with_one_element.insert(
            None, self.node1_12)
        self.assertEqual(
            3, self.LinkedListWihtDummyNodes_with_one_element.len())
        self.assertEqual(self.node1_11.next, self.node1_12)
        self.assertEqual(self.node1_12.prev, self.node1_11)

    def test_insert_LinkedListWihtDummyNodes_with_10_elements(self):
        self.LinkedListWihtDummyNodes_with_10_elements.insert(
            None, self.node1_11)
        self.assertEqual(
            11, self.LinkedListWihtDummyNodes_with_10_elements.len())
        self.assertEqual(self.node_10.next, self.node1_11)
        self.assertEqual(self.node1_11.prev, self.node_10)

        self.LinkedListWihtDummyNodes_with_10_elements.insert(
            self.node_3, self.node1_12)
        self.assertEqual(
            12, self.LinkedListWihtDummyNodes_with_10_elements.len())
        self.assertEqual(self.node1_12.next, self.node_4)
        self.assertEqual(self.node1_12.prev, self.node_3)
        self.assertEqual(self.node_4.prev, self.node1_12)

    # метод add_in_head
    def test_add_in_head_empty_LinkedListWihtDummyNodes(self):
        self.empty_LinkedListWihtDummyNodes.add_in_head(self.node)
        self.assertEqual(self.empty_LinkedListWihtDummyNodes.len(), 1)

    def test_add_in_head_LinkedListWihtDummyNodes_with_one_element(self):
        self.LinkedListWihtDummyNodes_with_one_element.add_in_head(
            self.node1_11)
        self.assertEqual(
            self.LinkedListWihtDummyNodes_with_one_element.len(), 2)
        self.assertEqual(self.node.prev, self.node1_11)
        self.assertEqual(self.node1_11.next, self.node)

    def test_add_in_head_LinkedListWihtDummyNodes_with_10_elements(self):
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_head(self.node)
        self.assertEqual(
            self.LinkedListWihtDummyNodes_with_10_elements.len(), 11)
        self.assertEqual(self.node.next, self.node_1)
        self.assertEqual(self.node_1.prev, self.node)

    def test_add_in_head_LinkedListWihtDummyNodes_with_10_elements_2(self):
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_head(self.node)
        self.LinkedListWihtDummyNodes_with_10_elements.add_in_head(
            self.node1_11)
        self.assertEqual(
            self.LinkedListWihtDummyNodes_with_10_elements.len(), 12)
        self.assertEqual(self.node.next, self.node_1)
        self.assertEqual(self.node_1.prev, self.node)
        self.assertEqual(self.node.prev, self.node1_11)
        self.assertEqual(self.node1_11.next, self.node)


if __name__ == '__main__':
    unittest.main()
