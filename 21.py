# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pointer = ListNode()
        pre_head = pointer

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    pointer.next = l1
                    l1 = l1.next
                else:
                    pointer.next = l2
                    l2 = l2.next
            else:
                if l1:
                    pointer.next = l1
                    l1 = l1.next
                else:
                    pointer.next = l2
                    l2 = l2.next

            pointer = pointer.next

        return pre_head.next
