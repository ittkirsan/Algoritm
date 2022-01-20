'''Программа реализации класса Стек'''
from LList2 import *


class Stack:
    '''Класс представления стека используем динамическую структуру - двунаправленный список.'''

    def __init__(self):
        self.stack = LinkedList2()

    def size(self):
        '''Метод определения длинны.'''
        return self.stack.len()

    def pop(self):
        '''Метод удаления последнего элемента'''
        if self.stack.len() != 0:
            result = self.stack.tail.value
            self.stack.del_tail()
            return result
        else:
            return None

    def push(self, value):
        '''Метод вставки в хвост.'''
        self.stack.add_in_tail(Node(value))

    def peek(self):
        '''Метод показывает последний элемент.'''
        if self.stack.len() != 0:
            return self.stack.tail.value
        else:
            return None
