'''Двунаправленные списки'''
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


class LinkedList2:
    '''Класс для представления двунаправленных списков.'''

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        '''Метод добавления узла в конец списка.'''
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    # 2.1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению.
    def find(self, val):
        '''Mетод поиска первого узла по его значению.'''
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # 2.2. Добавьте в класс LinkedList2 метод поиска всех узлов
    # по конкретному значению (возвращается список найденных узлов).
    def find_all(self, val):
        '''Mетод поиска всех узлов по конкретному значению. Возращает список Node'''
        result: list = []
        node = self.head  # находимся в начале списка
        while node is not None:  # итерация по списку
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        '''Метод удаления одого или всех узлов по значению.'''
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is None:
                    self.head = node.next
                else:
                    node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev

                if not all:
                    return
            node = node.next

    # 2.7. Добавьте в класс LinkedList2 метод очистки всего содержимого (создание пустого списка)
    def clean(self):
        '''Метод очистки списка.'''
        self.head = None
        self.tail = None

    # 2.8. Добавьте в класс LinkedList2 метод вычисления текущей длины списка
    def len(self):
        '''Метод вычесления длинны двунаправленного списка. Возвращает длинну списка.'''
        count: int = 0
        node = self.head
        if self.head is None:  # если список пустой сразу выходим со значением 0
            return 0

        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, after_node, new_node):
        '''Метод вставки узла в список в конец, если after_node = None, или после него.'''

        if after_node is None:
            if self.head is None:
                self.head = new_node
                self.tail = new_node

            else:
                self.tail.next, new_node.prev = new_node, self.tail
                self.tail = new_node

        elif after_node is self.tail:
            self.tail.next = new_node
            self.tail, self.tail.prev = new_node, self.tail

        else:
            after_node.next, new_node.next = new_node, after_node.next
            new_node.prev = after_node

    def add_in_head(self, new_node):
        '''Метод вставки узла в начало списка.'''
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            new_node.prev = None
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
