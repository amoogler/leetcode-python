# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num, pointer = 0, head

        while pointer:
            num |= pointer.val

            if not pointer.next:
                return num

            num <<= 1
            pointer = pointer.next

        return num
