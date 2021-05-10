# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         def getMaxDepth(node: TreeNode) -> int:
#             if not node:
#                 return 0

#             return max(getMaxDepth(node.left), getMaxDepth(node.right)) + 1

#         stack = [root]
#         diameter = 0

#         while stack:
#             node = stack.pop()
#             diameter = max(getMaxDepth(node.left) + getMaxDepth(node.right), diameter)

#             if node.left:
#                 stack.append(node.left)

#             if node.right:
#                 stack.append(node.right)

#         return diameter

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def getLongestPath(node: TreeNode) -> int:
            if not node:
                return 0

            left_path = getLongestPath(node.left)
            right_path = getLongestPath(node.right)
            diameter[0] = max(diameter[0], left_path + right_path)

            return max(left_path, right_path) + 1

        diameter = [0]
        getLongestPath(root)

        return diameter[0]

