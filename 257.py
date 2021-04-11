# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths, path = [], []
        self.dfs(root, path, paths)
        return paths

    def dfs(self, node: TreeNode, path: List[str], paths: List[str]):
        if not node:
            return

        if not node.left and not node.right:
            path.append(str(node.val))
            paths.append(''.join(path))

        self.dfs(node.left, path + [str(node.val), "->"], paths)
        self.dfs(node.right, path + [str(node.val), "->"], paths)
