# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Top-down Approach.
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node: 'TreeNode') -> int:
            if not node:
                return -1

            curr_height = 1 + max(dfs(node.left), dfs(node.right))

            if curr_height == len(res):
                res.append([])

            res[curr_height].append(node.val)
            node.left, node.right = None, None
            return curr_height

        dfs(root)

        return res
