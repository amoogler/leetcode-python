"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            # If node has a right child, the successor is
            # somewhere lower in the right subtree. Go right,
            # then go as many times to left as possible.
            node = node.right

            while node.left:
                node = node.left

            return node
        else:
            # If node has no right child, the successor is
            # somewhere in the upper level. Go up till the
            # node is left child of its parent, the parent
            # is the successor.
            while node.parent and node == node.parent.right:
                node = node.parent

            return node.parent
