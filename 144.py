# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         preorder_nodes = []
#         self.preorder(root, preorder_nodes)

#         return preorder_nodes

#     def preorder(self, node: TreeNode, preorder_nodes: List[int]):
#         if node:
#             preorder_nodes.append(node.val)
#             self.preorder(node.left, preorder_nodes)
#             self.preorder(node.right, preorder_nodes)

# Iterative
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         preorder_nodes, stack = [], []
#         current = root

#         while stack or current:
#             if current:
#                 preorder_nodes.append(current.val)
#                 stack.append(current)
#                 current = current.left
#             else:
#                 node = stack.pop()
#                 current = node.right

#         return preorder_nodes

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        preorder_nodes, stack = [], [root]

        while stack:
            node = stack.pop()

            if node:
                preorder_nodes.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return preorder_nodes
