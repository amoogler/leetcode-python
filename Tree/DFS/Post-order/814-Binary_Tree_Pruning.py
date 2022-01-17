# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode) -> bool:
            if not node:
                return False

            left, right = dfs(node.left), dfs(node.right)

            if not left and not right:
                node.left = None
                node.right = None
                return node.val == 1
            elif not left:
                node.left = None
            elif not right:
                node.right = None

            return True

        return root if dfs(root) else None
