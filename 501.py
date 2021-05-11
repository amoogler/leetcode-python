# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def pushleft(stack: List[TreeNode], node: TreeNode):
            while node:
                stack.append(node)
                node = node.left

        modes = []
        counter = collections.defaultdict(int)
        stack = []
        pushleft(stack, root)

        while stack:
            node = stack.pop()
            counter[node.val] += 1
            pushleft(stack, node.right)

        mode_count = max(counter.values())

        for k, v in counter.items():
            if v == mode_count:
                modes.append(k)

        return modes
