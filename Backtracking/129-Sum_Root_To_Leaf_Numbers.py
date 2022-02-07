# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def backtrack(node: TreeNode, path_num: int) -> None:
            nonlocal leaf_sum

            # Base cases.
            if not node:
                return

            if not node.left and not node.right:
                path_num = path_num * 10 + node.val
                leaf_sum += path_num
                path_num = (path_num - node.val) // 10

            # Recursive steps.
            path_num = path_num * 10 + node.val
            backtrack(node.left, path_num)
            backtrack(node.right, path_num)
            path_num = (path_num - node.val) // 10

        leaf_sum = 0
        backtrack(root, 0)
        return leaf_sum
