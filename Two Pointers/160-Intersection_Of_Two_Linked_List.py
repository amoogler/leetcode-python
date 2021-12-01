# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointA, pointB = headA, headB

        while pointA != pointB:
            if pointA:
                pointA = pointA.next
            else:
                pointA = headB

            if pointB:
                pointB = pointB.next
            else:
                pointB = headA

        return pointA
