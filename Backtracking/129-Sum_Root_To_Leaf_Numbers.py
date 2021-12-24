# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        leaf_sum = [0]
        self.backtrack(root, leaf_sum, 0)
        return leaf_sum[0]

    def backtrack(self, node: TreeNode, leaf_sum: List[int], path_num: int) -> None:
        # Base cases.
        if not node:
            return

        if not node.left and not node.right:
            path_num = path_num * 10 + node.val
            leaf_sum[0] += path_num
            path_num = (path_num - node.val) // 10

        # Recursive steps.
        path_num = path_num * 10 + node.val
        self.backtrack(node.left, leaf_sum, path_num)
        self.backtrack(node.right, leaf_sum, path_num)
        path_num = (path_num - node.val) // 10
