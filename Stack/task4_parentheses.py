'''Функция для определения сбалансированности скобочного рядаю'''
from task4_stack_tail import *


def parentheses(string: str):
    stack = Stack()
    for i in string:
        if i in '(':
            stack.push(i)
        else:  # удаляем пару
            if stack.pop() is None:
                return False
    return stack.size() == 0
