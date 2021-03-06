'''Функция, которая с помощью двух стеков реализует вычислениепостфиксных выражений.'''
from task4_stack_tail import Stack


def postfix(string: str):
    '''Функция, которая с помощью двух стеков реализует вычислениепостфиксных выражений'''
    stack1 = Stack()
    stack2 = Stack()
    length: int = len(string)-1
    while length >= 0:
        stack1.push(string[length])
        length -= 1
    while stack1.size() != 0:
        elem: str = stack1.pop()
        if elem.isdecimal():
            stack2.push(elem)
        elif elem in "+-*/":
            x: int = int(stack2.pop())
            y: int = int(stack2.pop())
            if elem == "+":
                stack2.push(x+y)
            elif elem == "*":
                stack2.push(x*y)
            elif elem == "-":
                stack2.push(x-y)
            elif elem == "/":
                stack2.push(x/y)
        elif elem == "=":
            return stack2.pop()
    return stack2.pop()
