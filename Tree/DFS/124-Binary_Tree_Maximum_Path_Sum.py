# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path = float('-inf')
        max_path = self.getMaxGain(root)
        return self.max_path

    def getMaxGain(self, node: TreeNode) -> int:
        if not node:
            return 0

        gain_left = max(self.getMaxGain(node.left), 0)
        gain_right = max(self.getMaxGain(node.right), 0)

        curr_max_path = node.val + gain_left + gain_right
        self.max_path = max(self.max_path, curr_max_path)

        return node.val + max(gain_left, gain_right)
