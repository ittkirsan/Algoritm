'''Класс передоставления двухсторонней очереди.'''
from typing import Any
'''
Как будет различаться мера сложности:
    add_item_in_head - O(n) / delete_head - O(n)
    aadd_item_in_tail - O(1) / removeTail - O(1)
При добавлении/удалении элемента в хвост нет необходимости перемещать все элементы списка, поэтому 
сложность у них O(1).
'''


class Deque:
    def __init__(self):
        '''Инициализация внутреннего хранилища.'''
        self.deque = []

    def add_item_in_head(self, item: Any):
        '''Метод добавления элемента в голову.'''
        self.deque.insert(0, item)

    def add_item_in_tail(self, item):
        '''Метод добавления элемента в хвост.'''
        self.deque.append(item)

    def delete_head(self):
        '''Метод удаления элемента из головы.'''
        if self.len_deque() != 0:
            return self.deque.pop(0)
        return None  # если очередь пуста

    def removeTail(self):
        '''Метод удаления элемента из хвоста.'''
        if self.len_deque() != 0:
            return self.deque.pop()
        return None  # если очередь пуста

    def len_deque(self):
        '''Метод определения длинны очереди.'''
        return len(self.deque)
