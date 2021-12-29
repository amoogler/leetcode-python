# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def lca(root, nodes) -> TreeNode:
            if not root:
                return None

            if any(root == node for node in nodes):
                return root

            left = lca(root.left, nodes)
            right = lca(root.right, nodes)

            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right

        return lca(root, nodes)
