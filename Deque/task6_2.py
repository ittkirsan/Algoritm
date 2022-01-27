'''Функция, которая с помощью deque проверяет, является ли некоторая строка палиндромом. '''

from task6 import *


def palindrome(string: str):
    deq = Deque()
    string = string.replace(' ', '')
    string = string.lower()
    for i in string:
        deq.addTail(i)
    for i in range(deq.size() // 2):
        if deq.removeFront() != deq.removeTail():
            return False
    return True
