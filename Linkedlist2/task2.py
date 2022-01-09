
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    # 2.1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению.
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # 2.2. Добавьте в класс LinkedList2 метод поиска всех узлов
    # по конкретному значению (возвращается список найденных узлов).
    def find_all(self, val):
        result = []
        node = self.head  # находимся в начале списка
        while node is not None:  # итерация по списку
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev == None:
                    self.head = node.next
                else:
                    node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev

                if not all:
                    return
            node = node.next

        # 2.7. Добавьте в класс LinkedList2 метод очистки всего содержимого (создание пустого списка)

    def clean(self):
        self.head = None
        self.tail = None

    # 2.8. Добавьте в класс LinkedList2 метод вычисления текущей длины списка
    def len(self):
        count = 0
        node = self.head
        if self.head is None:  # если список пустой сразу выходим со значением 0
            return 0

        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):

        if afterNode is None:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
                return None
            else:
                self.tail.next, newNode.prev = newNode, self.tail
                self.tail = newNode
                return

        node = self.head
        while node is not None:
            if node is afterNode:
                if node is self.tail:
                    self.tail, self.tail.prev = newNode, self.tail
                node.next, newNode.next = newNode, node.next
                newNode.prev = node
                return None
            node = node.next
        return None

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
