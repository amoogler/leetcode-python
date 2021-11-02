# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Top-Down Recursion
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         def getTreeDepth(node: TreeNode) -> int:
#             if not node:
#                 return 0

#             return max(getTreeDepth(node.left), getTreeDepth(node.right)) + 1

#         if not root:
#             return True

#         if abs(getTreeDepth(root.left) - getTreeDepth(root.right)) > 1:
#             return False

#         return self.isBalanced(root.left) and self.isBalanced(root.right)

# Bottom-up Recursion
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node: TreeNode) -> (bool, int):
            if not node:
                return True, 0

            left_ok, left_depth = helper(node.left)
            right_ok, right_depth = helper(node.right)

            if not left_ok or not right_ok:
                return False, 0

            return (abs(left_depth - right_depth) < 2), 1 + max(left_depth, right_depth)

        return helper(root)[0]
