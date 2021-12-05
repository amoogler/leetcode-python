# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        faster = head
        slow = dummy

        if not head or not head.next:
            return None

        while faster and faster.next:
            slow = slow.next
            faster = faster.next.next

        slow.next = slow.next.next

        return dummy.next
