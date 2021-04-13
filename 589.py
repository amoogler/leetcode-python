"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        preorder_nodes = []
        self.get_preorder(root, preorder_nodes)
        return preorder_nodes

    def get_preorder(self, node: 'Node', preorder_nodes: List[int]):
        if node:
            preorder_nodes.append(node.val)

            for child in node.children:
                self.get_preorder(child, preorder_nodes)
