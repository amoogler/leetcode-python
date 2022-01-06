# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(node) -> int:
            nonlocal count

            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            if left + right == node.val:
                count += 1

            return left + right + node.val

        dfs(root)
        return count
