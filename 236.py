# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS Recursive Solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, p, q):
            # Base cases.
            if not root:
                return None

            if root == p or root == q:
                return root

            # Recursive steps.
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)

            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right

        return lca(root, p, q)
