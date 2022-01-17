# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []

        def dfs(root: 'TreeNode', is_root: bool) -> 'TreeNode':
            if not root:
                return None

            # Add node into res upon node is root and no deletion needed.
            deletion_needed = root.val in to_delete_set

            if is_root and not deletion_needed:
                res.append(root)

            root.left = dfs(root.left, deletion_needed)
            root.right = dfs(root.right, deletion_needed)

            return None if deletion_needed else root

        dfs(root, True)
        return res
