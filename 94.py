# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         inorder_nodes = []
#         self.inorder(root, inorder_nodes)
#         return inorder_nodes

#     def inorder(self, node: TreeNode, inorder_nodes: List[int]):
#         if not node:
#             return

#         self.inorder(node.left, inorder_nodes)
#         inorder_nodes.append(node.val)
#         self.inorder(node.right, inorder_nodes)

# Iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder_nodes, stack = [], []
        current = root

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                inorder_nodes.append(node.val)
                current = node.right

        return inorder_nodes
