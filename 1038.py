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
                node = node.left

        stack, nodes, total_sum = [], [], 0
        pushleft(stack, root)

        while stack:
            node = stack.pop()
            total_sum += node.val
            nodes.append(node)
            pushleft(stack, node.right)

        for node in nodes:
            temp = node.val
            node.val = total_sum
            total_sum -= temp

        return root
