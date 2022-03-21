# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode(-1)
        p1, p2 = head, head
        curr_sum = 0

        while p2:

            if p2.val != 0:
                curr_sum += p2.val
            elif p2.val == 0 and p1 != p2:
                node = ListNode(curr_sum)
                node.next = p2
                p1.next = node
                curr_sum = 0
                p1 = p2

            p2 = p2.next

        pre = ListNode(-1)
        pre.next = head
        p = pre

        while p and p.next:
            if p.next.val != 0:
                p = p.next
            else:
                p.next = p.next.next

        return pre.next
