# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths, curr_path = [], []
        self.dfs(root, targetSum, curr_path, paths)
        return paths

    def dfs(self, node: TreeNode, targetSum: int, curr_path: List[int], paths: List[List[int]]):
        if not node:
            return

        if not node.left and not node.right and node.val == targetSum:
            curr_path.append(node.val)
            paths.append(curr_path)
            return

        self.dfs(node.left, targetSum - node.val, curr_path + [node.val], paths)
        self.dfs(node.right, targetSum - node.val, curr_path + [node.val], paths)
