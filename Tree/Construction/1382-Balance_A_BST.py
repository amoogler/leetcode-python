# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        # Inorder traverse the BST to a sorted list.
        def pushleft(stack: List, node: TreeNode):
            while node:
                stack.append(node)
                node = node.left

        stack = []
        pushleft(stack, root)
        sorted_list = []

        while stack:
            node = stack.pop()
            sorted_list.append(node.val)
            pushleft(stack, node.right)

        # Construct a balanced BST from sorted list.
        def helper(left: int, right: int) -> TreeNode:
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(sorted_list[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(sorted_list) - 1)
