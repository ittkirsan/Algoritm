
'''Программа реализации динамического массива.'''
from typing import Any


class Queue:
    '''Класс представления струтуры данных - очередь.'''

    def __init__(self):
        '''Инициализация хранилища данных.'''
        self.queue = []

    def enqueue(self, item: Any):
        '''Метод вставки элемента в хвост очереди.'''
        self.queue.append(item)

    def dequeue(self):
        '''Метод выдачи элемента из головы очереди.'''
        if self.size != 0:
            return self.queue.pop(0)
        return None  # если очередь пустая

    def size(self):
        '''Метод определения длинны очереди.'''
        return len(self.queue)
