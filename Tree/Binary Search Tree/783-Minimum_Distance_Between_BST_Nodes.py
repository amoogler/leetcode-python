# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_value = float('inf')
        prev_value = None

        def pushleft(stack, node):
            while node:
                stack.append(node)
                node = node.left

        stack = []
        pushleft(stack, root)

        while stack:
            node = stack.pop()

            # prev_value can be 0, so we need to explictly check None.
            if prev_value != None:
                min_value = min(min_value, node.val - prev_value)

            prev_value = node.val

            if node.right:
                pushleft(stack, node.right)

        return min_value
