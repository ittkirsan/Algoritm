from task1 import SimpleLinkedList, Node


def SumEqualLinkedList(LList1: SimpleLinkedList, LList2: SimpleLinkedList) -> SimpleLinkedList:
    LList_result: SimpleLinkedList = SimpleLinkedList()
    if LList1.len() == LList2.len():
        node1: Node = LList1.head  # вSimpleLinkedListстаем вначало списка 1
        node2: Node = LList2.head  # встаем вначало списка 2
        while node1 is not None:
            sum: int = node1.value + node2.value  # сумируем значение узлов
            # создаем узел и добавляем его в список
            LList_result.add_in_tail(Node(sum))
            node1, node2 = node1.next, node2.next
    return LList_result
