# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverseList(head: ListNode, tail: ListNode) -> ListNode:
            prev, curr = None, head

            while curr != tail:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev

        fast, slow = head, head
        start, end = head, ListNode()

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            end = reverseList(slow, fast.next)
        else:
            end = reverseList(slow, fast)

        while end:
            if start.val != end.val:
                return False

            start = start.next
            end = end.next

        return True
