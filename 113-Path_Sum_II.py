# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths, curr_path = [], []
        self.backtrack(root, targetSum, curr_path, paths)
        return paths

    def backtrack(self, node: TreeNode, targetSum: int, curr_path: List[int], paths: List[List[int]]):
        if not node:
            return

        if not node.left and not node.right and node.val == targetSum:
            curr_path.append(node.val)
            paths.append(curr_path[:])
            del curr_path[-1]
            return

        curr_path.append(node.val)
        self.backtrack(node.left, targetSum - node.val, curr_path, paths)
        self.backtrack(node.right, targetSum - node.val, curr_path, paths)
        del curr_path[-1]
