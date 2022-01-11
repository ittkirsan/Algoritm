'''Двунаправленный связанный список с двумя
фиктивными/пустыми узелами(dummy) в начале и в конце списка.
'''
from typing import Any


class Node:
    '''
    Класс для представления узла.
    v: данные(число или строка).
    '''

    def __init__(self, val: Any):
        '''Устанавливает все необходимые атрибуты для Node.'''
        self.value = val
        self.prev = None
        self.next = None


class DummyNode(Node):
    '''Класс для представления пустых узлов.'''

    def __init__(self):
        '''Наследует атртбуты Node.'''
        super().__init__(None)


class LinkedListWihtDummyNodes:
    '''Класс для представления двунаправленных списков.'''

    def __init__(self):
        '''Устанавливает необходимые атрибуты для  двунаправленного списка.'''
        self.head_dummy = DummyNode()
        self.tail_dummy = DummyNode()
        self.head_dummy.next = self.tail_dummy
        self.tail_dummy.prev = self.head_dummy

    def clean(self):
        '''Метод очистки списка.'''
        self.head_dummy = DummyNode()
        self.tail_dummy = DummyNode()
        self.head_dummy.next = self.tail_dummy
        self.tail_dummy.prev = self.head_dummy

    def find(self, val):
        '''Mетод поиска первого узла по его значению.'''
        node = self.head_dummy.next
        while node is not self.tail_dummy:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        '''Mетод поиска всех узлов по конкретному значению. Возращает список Node'''
        result: list = []
        node = self.head_dummy.next  # находимся в начале списка
        while node is not self.tail_dummy:  # итерация по списку
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def len(self):
        '''Метод вычесления длинны двунаправленного списка. Возвращает длинну списка.'''
        count: int = 0
        node = self.head_dummy.next
        while node is not self.tail_dummy:
            count += 1
            node = node.next
        return count

    def add_in_tail(self, item):
        '''Метод добавления узла в конец списка.'''
        tmp = self.tail_dummy.prev
        self.tail_dummy.prev.next = item
        self.tail_dummy.prev = item
        item.next = self.tail_dummy
        item.prev = tmp

    def delete(self, val, all=False):
        '''Метод удаления одого или всех узлов по значению.'''
        node = self.head_dummy.next
        while node is not self.tail_dummy:
            if node.value == val:
                node.prev.next, node.next.prev = node.next, node.prev
                if all is not True:
                    return
            node = node.next

    def insert(self, after_node, new_node):
        '''Метод вставки узла в список в конец, если after_node = None, или после него.'''

        if after_node is None:
            self.tail_dummy.prev.next = new_node
            self.tail_dummy.prev, new_node.prev = new_node, self.tail_dummy.prev
            new_node.next = self.tail_dummy
        else:
            after_node.next.prev = new_node
            after_node.next, new_node.next = new_node, after_node.next
            new_node.prev = after_node

    def add_in_head(self, new_node):
        '''Метод вставки узла в начало списка.'''
        self.head_dummy.next.prev = new_node
        self.head_dummy.next, new_node.next = new_node, self.head_dummy.next
        new_node.prev = self.head_dummy
