"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def pushleft(stack: List[Node], node: Node) -> None:
            while node:
                stack.append(node)
                node = node.left

        if not root:
            return None

        stack = []
        pushleft(stack, root)
        first, curr, pre = None, None, None

        while stack:
            curr = stack.pop()

            if not first:
                first = curr

            if pre:
                pre.right = curr
                pre.right.left = pre

            pre = curr
            pushleft(stack, curr.right)

        curr.right = first
        curr.right.left = curr

        return first
