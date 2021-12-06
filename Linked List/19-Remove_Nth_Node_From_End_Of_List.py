# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        fast = head
        slow = dummy

        # Move fast pointer by n steps.
        while n > 0:
            fast = fast.next
            n -= 1

        # Move both pointers together until fast reaches None.
        while fast:
            fast = fast.next
            slow = slow.next

        # Delete the node.
        slow.next = slow.next.next

        return dummy.next
