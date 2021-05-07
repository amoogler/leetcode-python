# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def pushleft(node: TreeNode, stack: List[TreeNode]):
            while node:
                stack.append(node)
                node = node.left

        stack = []
        pushleft(root, stack)
        res = curr_node = TreeNode(None)

        while stack:
            node = stack.pop()
            node.left = None
            curr_node.right = node
            curr_node = curr_node.right
            pushleft(node.right, stack)

        return res.right
