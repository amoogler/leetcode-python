# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    p_found, q_found = False, False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, p, q):
            if not root:
                return None

            # Search entire tree first.
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)

            if root == p:
                self.p_found = True
                return root

            if root == q:
                self.q_found = True
                return root

            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right

        lca = lca(root, p, q)
        return lca if self.p_found and self.q_found else None
