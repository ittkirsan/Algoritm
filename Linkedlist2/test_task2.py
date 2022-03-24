'''Тесты для task2. Двунаправленный список.'''
import unittest
import random
from task2 import Node, DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):
    '''Класс для тестов DoubleLinkedList'''

    def setUp(self):
        '''Вводные инструкции'''
        self.empty_DoubleLinkedList = DoubleLinkedList()

        self.DoubleLinkedList_with_one_element = DoubleLinkedList()
        self.node = Node(33)
        self.node1_11 = Node(15)
        self.node1_12 = Node(16)
        self.DoubleLinkedList_with_one_element.add_in_tail(self.node)

        self.DoubleLinkedList_with_10_elements = DoubleLinkedList()
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
        self.DoubleLinkedList_with_10_elements.add_in_tail(self.node_1)
        self.DoubleLinkedList_with_10_elements.add_in_tail(self.node_2)
        self.DoubleLinkedList_with_10_elements.add_in_tail(self.node_3)
        self.DoubleLinkedList_with_10_elements.add_in_tail(self.node_4)
        self.DoubleLinkedList_with_10_elements.add_in_tail(self.node_5)
        self.DoubleLinkedList_with_10_elements.add_in_tail(self.node_6)
        self.DoubleLinkedList_with_10_elements.add_in_tail(self.node_7)
        self.DoubleLinkedList_with_10_elements.add_in_tail(self.node_8)
        self.DoubleLinkedList_with_10_elements.add_in_tail(self.node_9)
        self.DoubleLinkedList_with_10_elements.add_in_tail(self.node_10)

        self.DoubleLinkedList_many_elements = DoubleLinkedList()
        self.N = random.randint(1, 200)
        for i in range(self.N):
            self.DoubleLinkedList_many_elements.add_in_tail(
                Node(random.randint(1, 500)))

    # метод len()

    def test_len_empty_DoubleLinkedList(self):
        self.assertEqual(0, self.empty_DoubleLinkedList.len())

    def test_len_DoubleLinkedList_with_one_element(self):
        self.assertEqual(1, self.DoubleLinkedList_with_one_element.len())

    def test_len_DoubleLinkedList_with_10_elements(self):
        self.assertEqual(10, self.DoubleLinkedList_with_10_elements.len())

    # метод clean()
    def test_clean_empty_DoubleLinkedList(self):
        self.empty_DoubleLinkedList.clean()
        self.assertEqual(None, self.empty_DoubleLinkedList.head)
        self.assertEqual(None, self.empty_DoubleLinkedList.tail)

    def test_clean_list_with_one_element(self):
        self.DoubleLinkedList_with_one_element.clean()
        self.assertEqual(None, self.DoubleLinkedList_with_one_element.head)
        self.assertEqual(None, self.DoubleLinkedList_with_one_element.tail)

    def test_clean_DoubleLinkedList_with_10_elements(self):
        self.DoubleLinkedList_with_10_elements.clean()
        self.assertEqual(None, self.DoubleLinkedList_with_10_elements.head)
        self.assertEqual(None, self.DoubleLinkedList_with_10_elements.tail)

    def test_clean_DoubleLinkedList_many_elements(self):
        length = self.DoubleLinkedList_many_elements.len()
        self.DoubleLinkedList_many_elements.clean()
        self.assertNotEqual(length, self.DoubleLinkedList_many_elements.len())
        self.assertEqual(0, self.DoubleLinkedList_many_elements.len())

   # метод find_all()

    def test_find_all_empty_DoubleLinkedList(self):
        self.assertEqual([], self.empty_DoubleLinkedList.find_all(10))
        self.assertEqual([], self.empty_DoubleLinkedList.find_all(25))
        self.assertEqual([], self.empty_DoubleLinkedList.find_all(1564))

    def test_find_all_DoubleLinkedList_with_one_element(self):
        self.assertEqual(
            [], self.DoubleLinkedList_with_one_element.find_all(155))
        self.assertEqual(
            [self.node], self.DoubleLinkedList_with_one_element.find_all(33))

    def test_find_all_DoubleLinkedList_with_10_elements(self):
        self.assertEqual([self.node_4, self.node_7, self.node_9],
                         self.DoubleLinkedList_with_10_elements.find_all(440))
        self.assertEqual(
            [self.node_3], self.DoubleLinkedList_with_10_elements.find_all(25))
        self.assertEqual(
            [], self.DoubleLinkedList_with_10_elements.find_all(1567))
        self.assertEqual(
            [], self.DoubleLinkedList_with_10_elements.find_all(0))

    # метод delete

    def test_delete_empty_DoubleLinkedList_false(self):
        self.empty_DoubleLinkedList.delete(15)
        self.assertEqual(None, self.empty_DoubleLinkedList.head)
        self.assertEqual(None, self.empty_DoubleLinkedList.tail)

    def test_delete_DoubleLinkedList_with_one_element_false(self):

        self.DoubleLinkedList_with_one_element.delete(15)
        self.assertEqual(
            self.node, self.DoubleLinkedList_with_one_element.head)
        self.assertEqual(
            self.node, self.DoubleLinkedList_with_one_element.tail)
        self.assertEqual(self.node.prev, None)

        self.DoubleLinkedList_with_one_element.delete(33)
        self.assertEqual(None, self.DoubleLinkedList_with_one_element.head)
        self.assertEqual(None, self.DoubleLinkedList_with_one_element.tail)

    def test_delete_DoubleLinkedList_with_10_elements_false(self):
        self.DoubleLinkedList_with_10_elements.delete(1532)
        self.assertEqual(10, self.DoubleLinkedList_with_10_elements.len())

        self.DoubleLinkedList_with_10_elements.delete(15)
        self.assertEqual(20, self.DoubleLinkedList_with_10_elements.head.value)
        self.assertEqual(self.node_2.prev, None)
        self.assertEqual(self.DoubleLinkedList_with_10_elements.len(), 9)

        self.DoubleLinkedList_with_10_elements.delete(5)
        self.assertEqual(
            440, self.DoubleLinkedList_with_10_elements.tail.value)
        self.assertEqual(
            self.DoubleLinkedList_with_10_elements.tail.prev, self.node_8)
        self.assertEqual(
            self.DoubleLinkedList_with_10_elements.tail.next, None)

        self.DoubleLinkedList_with_10_elements.delete(440)
        self.assertEqual(self.node_3.next, self.node_5)
        self.assertEqual(self.node_5.prev, self.node_3)
        self.assertEqual(self.node_7.value, 440)

    # удаление всех узлв с заданным значением
    def test_delete_empty_DoubleLinkedList_true(self):
        self.empty_DoubleLinkedList.delete(10, True)
        self.assertEqual(None, self.empty_DoubleLinkedList.head)
        self.assertEqual(None, self.empty_DoubleLinkedList.tail)

    def test_delete_DoubleLinkedList_with_one_element_true(self):
        self.DoubleLinkedList_with_one_element.delete(33, True)
        self.assertEqual(None, self.DoubleLinkedList_with_one_element.head)
        self.assertEqual(None, self.DoubleLinkedList_with_one_element.tail)
        self.assertEqual(None, self.DoubleLinkedList_with_10_elements.find(33))

    def test_delete_DoubleLinkedList_with_10_elements_true(self):
        self.DoubleLinkedList_with_10_elements.delete(154, True)
        self.assertEqual(10, self.DoubleLinkedList_with_10_elements.len())
        self.assertEqual(
            self.node_1, self.DoubleLinkedList_with_10_elements.head)
        self.assertEqual(
            self.node_10, self.DoubleLinkedList_with_10_elements.tail)

        self.DoubleLinkedList_with_10_elements.delete(440, True)
        self.assertEqual(7, self.DoubleLinkedList_with_10_elements.len())
        self.assertEqual(
            self.node_1, self.DoubleLinkedList_with_10_elements.head)
        self.assertEqual(
            self.node_10, self.DoubleLinkedList_with_10_elements.tail)
        self.assertEqual(
            None, self.DoubleLinkedList_with_10_elements.find(440))
        self.assertEqual(self.node_8.prev, self.node_6)
        self.assertEqual(self.node_8.next.value, 5)

    # метод insert()

    def test_insert_empty_DoubleLinkedList(self):
        self.empty_DoubleLinkedList.insert(None, self.node)
        self.assertEqual(1, self.empty_DoubleLinkedList.len())
        self.assertEqual(self.node, self.empty_DoubleLinkedList.head)
        self.assertEqual(self.node, self.empty_DoubleLinkedList.tail)
        self.assertEqual(self.node.next, None)
        self.assertEqual(self.node.prev, None)

    def test_insert_DoubleLinkedList_with_one_element(self):
        self.DoubleLinkedList_with_one_element.insert(self.node, self.node1_11)
        self.assertEqual(2, self.DoubleLinkedList_with_one_element.len())
        self.assertEqual(
            self.node, self.DoubleLinkedList_with_one_element.head)
        self.assertEqual(
            self.node1_11, self.DoubleLinkedList_with_one_element.tail)
        self.assertEqual(self.node1_11.prev, self.node)

        self.DoubleLinkedList_with_one_element.insert(None, self.node1_12)
        self.assertEqual(3, self.DoubleLinkedList_with_one_element.len())
        self.assertEqual(
            self.node, self.DoubleLinkedList_with_one_element.head)
        self.assertEqual(
            self.node1_12, self.DoubleLinkedList_with_one_element.tail)
        self.assertEqual(self.node1_11.next, self.node1_12)
        self.assertEqual(self.node1_12.prev, self.node1_11)

    def test_insert_DoubleLinkedList_with_10_elements(self):
        self.DoubleLinkedList_with_10_elements.insert(None, self.node1_11)
        self.assertEqual(11, self.DoubleLinkedList_with_10_elements.len())
        self.assertEqual(
            self.node_1, self.DoubleLinkedList_with_10_elements.head)
        self.assertEqual(
            self.node1_11, self.DoubleLinkedList_with_10_elements.tail)
        self.assertEqual(self.node_1.prev, None)

        self.DoubleLinkedList_with_10_elements.insert(
            self.node_3, self.node1_12)
        self.assertEqual(12, self.DoubleLinkedList_with_10_elements.len())
        self.assertEqual(
            self.node_1, self.DoubleLinkedList_with_10_elements.head)
        self.assertEqual(
            self.node1_11, self.DoubleLinkedList_with_10_elements.tail)
        self.assertEqual(self.node1_12.next, self.node_4)

    # метод add_in_head
    def test_add_in_head_empty_DoubleLinkedList(self):
        self.empty_DoubleLinkedList.add_in_head(self.node)
        self.assertEqual(self.node, self.empty_DoubleLinkedList.head)
        self.assertEqual(self.node, self.empty_DoubleLinkedList.tail)
        self.assertEqual(self.node.next, None)
        self.assertEqual(self.node.prev, None)

    def test_add_in_head_DoubleLinkedList_with_one_element(self):
        self.DoubleLinkedList_with_one_element.add_in_head(self.node1_11)
        self.assertEqual(
            self.node1_11, self.DoubleLinkedList_with_one_element.head)
        self.assertEqual(
            self.node, self.DoubleLinkedList_with_one_element.tail)
        self.assertEqual(self.node.next, None)
        self.assertEqual(self.node.prev, self.node1_11)
        self.assertEqual(self.node1_11.prev, None)

    def test_add_in_head_DoubleLinkedList_with_10_elements(self):
        self.DoubleLinkedList_with_10_elements.add_in_head(self.node)
        self.assertEqual(
            self.node, self.DoubleLinkedList_with_10_elements.head)
        self.assertEqual(
            self.node_10, self.DoubleLinkedList_with_10_elements.tail)
        self.assertEqual(self.node.next, self.node_1)
        self.assertEqual(self.node.prev, None)
        self.assertEqual(self.node_1.prev, self.node)


if __name__ == '__main__':
    unittest.main()
