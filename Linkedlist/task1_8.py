

def SumEqualLinkedList(LList1, LList2):
    LList_result = LinkedList()
    if LList1.len() == LList2.len():
        node1 = LList1.head # встаем вначало списка 1
        node2 = LList2.head # встаем вначало списка 2
        while node1 is not None:
            sum = node1.value + node2.value #сумируем значение узлов
            LList_result.add_in_tail(Node(sum)) # создаем узел и добавляем его в список
            node1, node2 = node1.next, node2.next 
        return LList_result