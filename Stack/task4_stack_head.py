'''Программа реализации класса Стек c головы.'''
from LList2 import *


class Stack:
    '''Класс представления стека используем динамическую структуру - двунаправленный список.'''

    def __init__(self):
        self.stack = LinkedList2()

    def size(self):
        '''Метод определения длинны.'''
        return self.stack.len()

    def pop(self):
        '''Метод удаления первого элемента'''
        if self.size() != 0:
            result = self.stack.head.value
            self.stack.del_head()
            return result
        elif self.size() == 0:
            return None

    def push(self, value):
        '''Метод вставки в начало.'''
        self.stack.add_in_head(Node(value))

    def peek(self):
        '''Метод показывает значение последнего элемента стека.'''
        if self.size() != 0:
            return self.stack.head.value
        else:
            return None
