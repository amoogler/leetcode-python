class Node:

    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pre_head = Node(0)


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        idx = 0
        pointer = self.pre_head

        while pointer.next and idx != index:
            pointer = pointer.next
            idx += 1

        return pointer.next.val if pointer.next and idx == index else -1


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        head = Node(val)
        head.next = self.pre_head.next
        self.pre_head.next = head


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        pointer = self.pre_head
        node = Node(val)

        while pointer.next:
            pointer = pointer.next

        node.next = pointer.next
        pointer.next = node


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        idx = 0
        pointer = self.pre_head
        node = Node(val)

        while pointer.next and idx != index:
            pointer = pointer.next
            idx += 1

        if idx == index:
            node.next = pointer.next
            pointer.next = node


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        idx = 0
        pointer = self.pre_head

        while pointer.next and idx != index:
            pointer = pointer.next
            idx += 1

        if pointer.next and idx == index:
            pointer.next = pointer.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
