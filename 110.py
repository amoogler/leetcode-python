# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getTreeDepth(node: TreeNode) -> int:
            if not node:
                return 0

            return max(getTreeDepth(node.left), getTreeDepth(node.right)) + 1

        if not root:
            return True

        if abs(getTreeDepth(root.left) - getTreeDepth(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
