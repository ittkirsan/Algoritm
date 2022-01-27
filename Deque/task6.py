'''Класс передоставления двухсторонней очереди.'''
from typing import Any
'''
Как будет различаться мера сложности:
    addFront - O(n) / removeFront - O(n)
    addTail - O(1) / removeTail - O(1)
При добавлении/удалении элемента в хвост нет необходимости перемещать все элементы списка, поэтому 
сложность у них O(1).
'''


class Deque:
    def __init__(self):
        '''Инициализация внутреннего хранилища.'''
        self.deque = []

    def addFront(self, item: Any):
        '''Метод добавления элемента в голову.'''
        self.deque.insert(0, item)

    def addTail(self, item):
        '''Метод добавления элемента в хвост.'''
        self.deque.append(item)

    def removeFront(self):
        '''Метод удаления элемента из головы.'''
        if self.size() != 0:
            return self.deque.pop(0)
        return None  # если очередь пуста

    def removeTail(self):
        '''Метод удаления элемента из хвоста.'''
        if self.size() != 0:
            return self.deque.pop()
        return None  # если очередь пуста

    def size(self):
        '''Метод определения длинны очереди.'''
        return len(self.deque)
