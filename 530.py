# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def pushleft(node: TreeNode, stack: List[TreeNode]):
            while node:
                stack.append(node)
                node = node.left

        stack = []
        pushleft(root, stack)
        min_diff = float('inf')
        prev_val = None

        while stack:
            node = stack.pop()

            if prev_val != None:
                diff = node.val - prev_val
                min_diff = min(min_diff, diff)

            prev_val = node.val
            pushleft(node.right, stack)

        return min_diff
