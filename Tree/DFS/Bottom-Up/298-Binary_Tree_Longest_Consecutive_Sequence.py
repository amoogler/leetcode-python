# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Top-down approach.
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, target, curr_length):
            if not node:
                return curr_length

            if node.val == target:
                curr_length += 1
            else:
                curr_length = 1

            left = dfs(node.left, node.val + 1, curr_length)
            right = dfs(node.right, node.val + 1, curr_length)

            return max(max(left, right), curr_length)

        return dfs(root, root.val, 0)

# Bottom-up approach.
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        global_max = 0

        def dfs(node):
            nonlocal global_max

            if not node:
                return 0

            curr_max = 1
            left, right = dfs(node.left), dfs(node.right)

            if node.left and node.val == node.left.val - 1:
                curr_max = max(curr_max, left + 1)

            if node.right and node.val == node.right.val - 1:
                curr_max = max(curr_max, right + 1)

            global_max = max(curr_max, global_max)
            return curr_max

        dfs(root)
        return global_max
