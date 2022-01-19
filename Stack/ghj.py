
from task4_stack_tail import *


def parentheses(string):
    S = Stack()
    for i in string:
        if i == '(':
            S.push(i)
        else:
            if S.pop() is None:
                return False
    return S.size() == 0


print(parentheses("(()((()()))"))
