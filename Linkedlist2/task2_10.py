'''
Фиктивный/пустой узел (dummy)
автор: Дмитриевич Вячеслав
'''


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self):
        super().__init__(None)


class LinkedListWihtDummyNodes:
    def __init__(self):
        self.head_dummy = DummyNode()
        self.tail_dummy = DummyNode()
        self.head_dummy.next = self.tail_dummy
        self.tail_dummy.prev = self.head_dummy

    def clean(self):
        self.head_dummy = DummyNode()
        self.tail_dummy = DummyNode()
        self.head_dummy.next = self.tail_dummy
        self.tail_dummy.prev = self.head_dummy

    def find(self, val):
        node = self.head_dummy.next
        while node is not self.tail_dummy:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head_dummy.next  # находимся в начале списка
        while node is not self.tail_dummy:  # итерация по списку
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def len(self):
        count = 0
        node = self.head_dummy.next
        while node is not self.tail_dummy:
            count += 1
            node = node.next
        return count

    def add_in_tail(self, item):
        tmp = self.tail_dummy.prev
        self.tail_dummy.prev.next = item
        self.tail_dummy.prev = item
        item.next = self.tail_dummy
        item.prev = tmp

    def delete(self, val, all=False):
        node = self.head_dummy.next
        while node is not self.tail_dummy:
            if node.value == val:
                node.prev.next, node.next.prev = node.next, node.prev
                if all != True:
                    return
            node = node.next

    def insert(self, afterNode, newNode):

        if afterNode is None:
            self.tail_dummy.prev.next = newNode
            self.tail_dummy.prev, newNode.prev = newNode, self.tail_dummy.prev
            newNode.next = self.tail_dummy

        node = self.head_dummy.next
        while node is not self.tail_dummy:
            if node is afterNode:
                node.next.prev = newNode
                node.next, newNode.next = newNode, node.next
                newNode.prev = node
                return None
            node = node.next
        return None

    def add_in_head(self, newNode):
        self.head_dummy.next.prev = newNode
        self.head_dummy.next, newNode.next = newNode, self.head_dummy.next
        newNode.prev = self.head_dummy
