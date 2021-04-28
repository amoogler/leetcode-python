# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        paths_sum = 0

        if not root:
            return paths_sum

        stack = [(root, 0)]

        while stack:
            node, curr = stack.pop()
            curr = (curr << 1) | node.val

            if not node.left and not node.right:
                paths_sum += curr
            else:
                if node.right:
                    stack.append((node.right, curr))

                if node.left:
                    stack.append((node.left, curr))

        return paths_sum
