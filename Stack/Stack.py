'''Класс представления стека.'''


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
        else:
            return None

    def add_item_in_tail(self, value):
        '''Метод вставки в хвост.'''
        self.stack.append(value)

    def peek(self):
        '''Метод показывает последний элемент.'''
        if self.size() != 0:
            return self.stack[-1]
        else:
            return None
