# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, curr_max: int, res: list):
            if not node:
                return

            if node.val >= curr_max:
                res[0] += 1
                curr_max = node.val

            dfs(node.left, curr_max, res)
            dfs(node.right, curr_max, res)

        res = [0]
        dfs(root, root.val, res)
        return res[0]
