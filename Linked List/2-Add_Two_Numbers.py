# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(0)
        current = prehead
        carry = 0
        node1, node2 = l1, l2

        while node1 or node2:
            if not node1:
                value_sum = node2.val + carry
                value = value_sum % 10
                carry = value_sum // 10
                current.next = ListNode(value)
                node2 = node2.next
            elif not node2:
                value_sum = node1.val + carry
                value = value_sum % 10
                carry = value_sum // 10
                current.next = ListNode(value)
                node1 = node1.next
            else:
                value_sum = node1.val + node2.val + carry
                value = value_sum % 10
                carry = value_sum // 10
                current.next = ListNode(value)
                node1 = node1.next
                node2 = node2.next

            current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return prehead.next
