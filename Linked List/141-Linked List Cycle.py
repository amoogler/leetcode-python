# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        faster, slower = head, head
        while faster.next and faster.next.next:
            faster = faster.next.next
            slower = slower.next
            
            if faster == slower:
                return True
        
        return False
