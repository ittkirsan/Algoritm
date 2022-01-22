'''Функция, которая "вращает" очередь по кругу на N элементов.'''
from task5 import Queue


def rotation(queue: Queue, N: int):
    if queue.size() > 0:
        for i in range(N):
            elem: = queue.dequeue()
            queue.enqueue(elem)
    return
