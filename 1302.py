# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        max_depth = self.getMaxDepth(root)
        depth, deep_sum = 1, 0

        if not root:
            return 0

        queue = collections.deque([root])

        while queue:
            level_length = len(queue)

            for _ in range(level_length):
                node = queue.popleft()

                if depth == max_depth:
                    deep_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            depth += 1

        return deep_sum

    def getMaxDepth(self, node: TreeNode) -> int:
        if not node:
            return 0

        return max(self.getMaxDepth(node.left), self.getMaxDepth(node.right)) + 1
