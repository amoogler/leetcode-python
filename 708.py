"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)

        if not head:
            node.next = node
            return node

        prev, curr = head, head.next

        while prev.next != head:
            if prev.val <= node.val <= curr.val:
                break

            if prev.val > curr.val and (node.val > prev.val or node.val < curr.val):
                break

            prev, curr = prev.next, curr.next

        # Insert node.
        node.next = curr
        prev.next = node

        return head
