'''Представление упорядоченного списка.'''


from typing import Any


class Node:
    '''
    Класс для представления узла.
    v: данные(число или строка).
    '''

    def __init__(self, val: Any):
        '''Устанавливает все необходимые атрибуты для Node.'''
        self._value = val
        self._prev = None
        self.next = None


class OrderedList:
    '''Класс для представления упорядоченных списков.'''

    def __init__(self, asc):
        '''Иницилизация списка.'''
        self.head = None
        self.tail = None
        self.__ascending = asc  # Упорядочение списка по возрастанию

    def compare(self, val_1: int, val_2: int):
        '''Метод сравнения чисел.'''
        if val_1 < val_2:
            return -1
        elif val_1 > val_2:
            return +1
        else:
            return 0

    def add_new_node_by_value(self, value):
        '''Метод добавления знаяения в положенное место.
         С учётом его значения и признака упорядоченности'''
        new_node = Node(value)
        if self.head is None:
            self.head, self.tail = new_node, new_node
            new_node._prev, new_node.next = None, None
            return None

        if self.__ascending:
            flag = 1
        else:
            flag = -1

        node = self.head
        while node is not None:
            if self.compare(node._value, value) == flag:
                if node == self.head:
                    new_node.next = self.head
                    self.head._prev = new_node
                    self.head = new_node
                    return None

                else:
                    node._prev.next = new_node
                    new_node._prev = node._prev
                    new_node.next = node
                    node._prev = new_node
                    return None
            node = node.next

        self.tail.next = new_node
        new_node._prev = self.tail
        self.tail = new_node

    def find_node_value(self, val):
        '''Метод поиска элемента по значению.С учетом возрастания функции или убывания.'''
        node = self.head
        if self.__ascending:
            flag = 1
        else:
            flag = -1
        while node is not None:
            if self.compare(node._value, val) == 0:
                return node
            elif self.compare(node._value, val) == flag:
                return None
            node = node.next
        return None

    def delete_node_value(self, val, all=False):
        '''Метод удаления одого или всех узлов по значению.'''
        node = self.head
        if self.__ascending:
            flag = 1
        else:
            flag = -1
        while node is not None:
            if self.compare(node._value, val) == flag:
                return
            if self.compare(node._value, val) == 0:
                if node._prev is None:
                    self.head = node.next
                else:
                    node._prev.next = node.next
                if node.next is not None:
                    node.next._prev = node._prev
                else:
                    self.tail = node._prev

                if not all:
                    return
            node = node.next

    def clean_orderlist(self, asc):
        '''Метод очистки списка.'''
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        '''Метод вычесления длинны упорядоченного списка. Возвращает длинну списка.'''
        count: int = 0
        node = self.head
        if self.head is None:  # если список пустой сразу выходим со значением 0
            return 0

        while node is not None:
            count += 1
            node = node.next
        return count

    def get_all(self):
        ol = []
        node = self.head
        while node is not None:
            ol.append(node)
            node = node.next
        return ol


class OrderedStringList(OrderedList):
    '''Наследник текущего класса, который будет упорядоченно хранить строки.'''

    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, val_1: str, val_2: str):
        string1: str = val_1.strip()
        string2: str = val_2.strip()
        if string1 < string2:
            return -1
        elif string1 > string2:
            return +1
        else:
            return 0
