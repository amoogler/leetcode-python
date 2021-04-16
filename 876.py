# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, faster = head, head

        while faster and faster.next:
            slow = slow.next
            faster = faster.next.next

        return slow
