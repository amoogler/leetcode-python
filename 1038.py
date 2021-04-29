# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def pushleft(stack: List[TreeNode], node: TreeNode):
            while node:
                stack.append(node)
                node = node.right

        stack, nodes, total_sum = [], [], 0
        pushleft(stack, root)

        while stack:
            node = stack.pop()
            total_sum += node.val
            node.val = total_sum
            nodes.append(node)
            pushleft(stack, node.left)

        return root
