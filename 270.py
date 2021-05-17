# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def closestValue(self, root: TreeNode, target: float) -> int:
#         def pushleft(stack: List[TreeNode], node: TreeNode):
#             while node:
#                 stack.append(node)
#                 node = node.left

#         stack = []
#         prev_value = float('-inf')
#         pushleft(stack, root)

#         while stack:
#             node = stack.pop()

#             if prev_value <= target <= node.val:
#                 return min(prev_value, node.val, key=lambda x: abs(target - x))

#             prev_value = node.val
#             pushleft(stack, node.right)

#         return prev_value

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val

        while root:
            closest = min(root.val, closest, key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right

        return closest
