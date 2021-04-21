# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def pushleft(stack: List[TreeNode], node: TreeNode):
            while node:
                stack.append(node)
                node = node.left

        stack, order = [], 1
        pushleft(stack, root)

        while stack:
            node = stack.pop()

            if order == k:
                return node.val

            order += 1
            pushleft(stack, node.right)
