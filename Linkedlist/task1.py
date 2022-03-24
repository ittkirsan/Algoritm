
class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class SimpleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    '''
    1.4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению
     (возвращается стандартный питоновский список найденных узлов).
    '''

    def find_all(self, val):
        result = []
        node = self.head  # находимся в начале списка
        while node is not None:  # итерация по списку
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    '''
    1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению 
    где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.
    1.2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
    '''

    def delete(self, val, all=False):

        if self.head is None:  # если список пустой сразу выходим
            return None

        while self.head.value == val:
            if self.head.next == None:
                self.__init__()
                return
            self.head = self.head.next
            if all is False:
                return

        node = self.head
        while node is not self.tail:
            if node.next.value == val:
                if node.next.next == None:
                    node.next = None
                    self.tail = node
                    return
                node.next = node.next.next
                if not all:
                    return
                continue
            node = node.next

    # 1.3. Добавьте в класс LinkedList метод очистки всего содержимого (создание пустого списка)
    def clean(self):
        self.head = None
        self.tail = None

    # 1.5. Добавьте в класс LinkedList метод вычисления текущей длины списка
    def len_simple_linkedList(self):
        count = 0
        if self.head is None:
            return 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    # Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode (из списка)
    def insert(self, afterNode, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return None

        if afterNode is None:
            self.head, newNode.next = newNode, self.head
            if newNode.next is None:
                self.tail = newNode
        else:
            node = self.head
            while node is not None:
                if node is afterNode:
                    if node is self.tail:
                        self.tail = newNode
                    node.next, newNode.next = newNode, node.next
                    return None
                node = node.next
        return None
