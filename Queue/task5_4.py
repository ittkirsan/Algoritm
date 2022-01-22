'''Реализация очереди с помощью двух стеков.'''
from typing import Any


class Queue2:
    '''Класс представления струтуры данных - очередь с помощью двух стеков.'''

    def __init__(self) -> None:
        '''Инициализация хранилища данных.'''
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item: Any):
        '''Метод вставки элемента в хвост очереди.'''
        self.stack1.push(item)

    def dequeue(self):
        '''Метод выдачи элемента из головы очереди.'''
        if not self.stack2.size():
            while self.stack1.size() > 0:
                elem = self.stack1.pop()
                self.stack2.push(elem)
        return self.stack2.pop()

    def size(self):
        '''Метод определения длинны очереди.'''
        return self.stack1.size() + self.stack2.size()


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        '''Метод определения длинны.'''
        return len(self.stack)

    def pop(self):
        '''Метод удаления последнего элемента'''
        if self.size() != 0:
            return self.stack.pop()
        return None

    def push(self, value):
        '''Метод вставки в хвост.'''
        self.stack.append(value)

    def peek(self):
        '''Метод показывает последний элемент.'''
        if self.size() != 0:
            return self.stack[-1]
        return None
