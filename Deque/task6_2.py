'''Функция, которая с помощью deque проверяет, является ли некоторая строка палиндромом. '''

from task6 import *


def palindrome(string: str):
    deq = Deque()
    string = string.replace(' ', '')
    string = string.lower()
    for i in string:
        deq.add_item_in_tail(i)
    for i in range(deq.len_deque() // 2):
        if deq.delete_head() != deq.removeTail():
            return False
    return True
