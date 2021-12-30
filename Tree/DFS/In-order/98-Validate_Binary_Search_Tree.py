# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def pushleft(node: TreeNode, stack: list[TreeNode]):
            while node:
                stack.append(node)
                node = node.left

        stack = []
        pushleft(root, stack)
        pre_node = None

        while stack:
            node = stack.pop()
            if pre_node and node.val <= pre_node.val:
                return False
            else:
                pre_node = node
                pushleft(node.right, stack)

        return True
