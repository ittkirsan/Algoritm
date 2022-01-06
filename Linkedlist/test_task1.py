
import unittest
import random
from task1 import Node, LinkedList
from task1_8 import SumEqualLinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.empty_LinkedList = LinkedList()

        self.LinkedList_with_one_element = LinkedList()
        self.node = Node(33)
        self.node1_11 = Node(15)
        self.node1_12 = Node(16)
        self.LinkedList_with_one_element.add_in_tail(self.node)

        self.LinkedList_with_10_elements = LinkedList()
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
        self.LinkedList_with_10_elements.add_in_tail(self.node_1)
        self.LinkedList_with_10_elements.add_in_tail(self.node_2)
        self.LinkedList_with_10_elements.add_in_tail(self.node_3)
        self.LinkedList_with_10_elements.add_in_tail(self.node_4)
        self.LinkedList_with_10_elements.add_in_tail(self.node_5)
        self.LinkedList_with_10_elements.add_in_tail(self.node_6)
        self.LinkedList_with_10_elements.add_in_tail(self.node_7)
        self.LinkedList_with_10_elements.add_in_tail(self.node_8)
        self.LinkedList_with_10_elements.add_in_tail(self.node_9)
        self.LinkedList_with_10_elements.add_in_tail(self.node_10)

        self.LinkedList_many_elements = LinkedList()
        self.N = random.randint(1, 200)
        for i in range(self.N):
            self.LinkedList_many_elements.add_in_tail(
                Node(random.randint(1, 500)))

        self.LinkedList_5_elem1 = LinkedList()
        self.LinkedList_5_elem2 = LinkedList()
        self.node_1s = Node(15)
        self.node_2s = Node(20)
        self.node_3s = Node(25)
        self.node_4s = Node(440)
        self.node_5s = Node(35)
        self.node_6s = Node(45)
        self.node_7s = Node(440)
        self.node_8s = Node(50)
        self.node_9s = Node(440)
        self.node_10s = Node(5)
        self.LinkedList_5_elem1.add_in_tail(self.node_1s)
        self.LinkedList_5_elem1.add_in_tail(self.node_2s)
        self.LinkedList_5_elem1.add_in_tail(self.node_3s)
        self.LinkedList_5_elem1.add_in_tail(self.node_4s)
        self.LinkedList_5_elem1.add_in_tail(self.node_5s)
        self.LinkedList_5_elem2.add_in_tail(self.node_6s)
        self.LinkedList_5_elem2.add_in_tail(self.node_7s)
        self.LinkedList_5_elem2.add_in_tail(self.node_8s)
        self.LinkedList_5_elem2.add_in_tail(self.node_9s)
        self.LinkedList_5_elem2.add_in_tail(self.node_10s)

    # метод len()

    def test_len_empty_LinkedList(self):
        self.assertEqual(0, self.empty_LinkedList.len())

    def test_len_LinkedList_with_one_element(self):
        self.assertEqual(1, self.LinkedList_with_one_element.len())

    def test_len_LinkedList_with_10_elements(self):
        self.assertEqual(10, self.LinkedList_with_10_elements.len())

    # метод clean()
    def test_clean_empty_LinkedList(self):
        self.empty_LinkedList.clean()
        self.assertEqual(None, self.empty_LinkedList.head)
        self.assertEqual(None, self.empty_LinkedList.tail)

    def test_clean_list_with_one_element(self):
        self.LinkedList_with_one_element.clean()
        self.assertEqual(None, self.LinkedList_with_one_element.head)
        self.assertEqual(None, self.LinkedList_with_one_element.tail)

    def test_clean_LinkedList_with_10_elements(self):
        self.LinkedList_with_10_elements.clean()
        self.assertEqual(None, self.LinkedList_with_10_elements.head)
        self.assertEqual(None, self.LinkedList_with_10_elements.tail)

    def test_clean_LinkedList_many_elements(self):
        length = self.LinkedList_many_elements.len()
        self.LinkedList_many_elements.clean()
        self.assertNotEqual(length, self.LinkedList_many_elements.len())
        self.assertEqual(0, self.LinkedList_many_elements.len())

   # метод find_all()

    def test_find_all_empty_LinkedList(self):
        self.assertEqual([], self.empty_LinkedList.find_all(10))
        self.assertEqual([], self.empty_LinkedList.find_all(25))
        self.assertEqual([], self.empty_LinkedList.find_all(1564))

    def test_find_all_LinkedList_with_one_element(self):
        self.assertEqual([], self.LinkedList_with_one_element.find_all(155))
        self.assertEqual(
            [self.node], self.LinkedList_with_one_element.find_all(33))

    def test_find_all_LinkedList_with_10_elements(self):
        self.assertEqual([self.node_4, self.node_7, self.node_9],
                         self.LinkedList_with_10_elements.find_all(440))
        self.assertEqual(
            [self.node_3], self.LinkedList_with_10_elements.find_all(25))
        self.assertEqual([], self.LinkedList_with_10_elements.find_all(1567))
        self.assertEqual([], self.LinkedList_with_10_elements.find_all(0))

    # метод delete

    def test_delete_empty_LinkedList_false(self):
        self.empty_LinkedList.delete(15)
        self.assertEqual(None, self.empty_LinkedList.head)
        self.assertEqual(None, self.empty_LinkedList.tail)

    def test_delete_LinkedList_with_one_element_false(self):

        self.LinkedList_with_one_element.delete(15)
        self.assertEqual(self.node, self.LinkedList_with_one_element.head)
        self.assertEqual(self.node, self.LinkedList_with_one_element.tail)

        self.LinkedList_with_one_element.delete(33)
        self.assertEqual(None, self.LinkedList_with_one_element.head)
        self.assertEqual(None, self.LinkedList_with_one_element.tail)

    def test_delete_LinkedList_with_10_elements_false(self):
        self.LinkedList_with_10_elements.delete(1532)
        self.assertEqual(10, self.LinkedList_with_10_elements.len())

        self.LinkedList_with_10_elements.delete(15)
        self.assertEqual(20, self.LinkedList_with_10_elements.head.value)

        self.LinkedList_with_10_elements.delete(5)
        self.assertEqual(440, self.LinkedList_with_10_elements.tail.value)

        self.LinkedList_with_10_elements.delete(440)
        self.assertEqual(self.node_3.next, self.node_5)

    # удаление всех узлв с заданным значением
    def test_delete_empty_LinkedList_true(self):
        self.empty_LinkedList.delete(10, True)
        self.assertEqual(None, self.empty_LinkedList.head)
        self.assertEqual(None, self.empty_LinkedList.tail)

    def test_delete_LinkedList_with_one_element_true(self):
        self.LinkedList_with_one_element.delete(33, True)
        self.assertEqual(None, self.LinkedList_with_one_element.head)
        self.assertEqual(None, self.LinkedList_with_one_element.tail)
        self.assertEqual(None, self.LinkedList_with_10_elements.find(33))

    def test_delete_LinkedList_with_10_elements_true(self):
        self.LinkedList_with_10_elements.delete(154, True)
        self.assertEqual(10, self.LinkedList_with_10_elements.len())
        self.assertEqual(self.node_1, self.LinkedList_with_10_elements.head)
        self.assertEqual(self.node_10, self.LinkedList_with_10_elements.tail)

        self.LinkedList_with_10_elements.delete(440, True)
        self.assertEqual(7, self.LinkedList_with_10_elements.len())
        self.assertEqual(self.node_1, self.LinkedList_with_10_elements.head)
        self.assertEqual(self.node_10, self.LinkedList_with_10_elements.tail)
        self.assertEqual(None, self.LinkedList_with_10_elements.find(440))

    # метод insert()
    def test_insert_empty_LinkedList(self):
        self.empty_LinkedList.insert(None, self.node)
        self.assertEqual(1, self.empty_LinkedList.len())
        self.assertEqual(self.node, self.empty_LinkedList.head)
        self.assertEqual(self.node, self.empty_LinkedList.tail)
        self.assertEqual(self.node.next, None)

    def test_insert_LinkedList_with_one_element(self):
        self.LinkedList_with_one_element.insert(self.node, self.node1_11)
        self.assertEqual(2, self.LinkedList_with_one_element.len())
        self.assertEqual(self.node, self.LinkedList_with_one_element.head)
        self.assertEqual(self.node1_11, self.LinkedList_with_one_element.tail)

        self.LinkedList_with_one_element.insert(None, self.node1_12)
        self.assertEqual(3, self.LinkedList_with_one_element.len())
        self.assertEqual(self.node1_12, self.LinkedList_with_one_element.head)
        self.assertEqual(self.node1_11, self.LinkedList_with_one_element.tail)
        self.assertEqual(self.node1_12.next, self.node)

    def test_insert_LinkedList_with_10_elements(self):
        self.LinkedList_with_10_elements.insert(None, self.node1_11)
        self.assertEqual(11, self.LinkedList_with_10_elements.len())
        self.assertEqual(self.node1_11, self.LinkedList_with_10_elements.head)
        self.assertEqual(self.node_10, self.LinkedList_with_10_elements.tail)

        self.LinkedList_with_10_elements.insert(self.node_3, self.node1_12)
        self.assertEqual(12, self.LinkedList_with_10_elements.len())
        self.assertEqual(self.node1_11, self.LinkedList_with_10_elements.head)
        self.assertEqual(self.node_10, self.LinkedList_with_10_elements.tail)
        self.assertEqual(self.node1_12.next, self.node_4)

    # функция суммы двух LinkedList

    def test_SumEqualLinkedList(self):
        #self.assertEqual([], SumEqualLinkedList(LinkedList(), self.empty_LinkedList))
        summa_Linkedlists = SumEqualLinkedList(
            self.LinkedList_5_elem1, self.LinkedList_5_elem2)
        self.assertEqual(5, summa_Linkedlists.len())
        self.assertEqual(60, summa_Linkedlists.head.value)
        self.assertEqual(40, summa_Linkedlists.tail.value)


if __name__ == '__main__':
    unittest.main()
