# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        averages = []

        if not root:
            return averages

        queue = collections.deque([root])

        while queue:
            level_length = len(queue)
            level_sum = 0

            for _ in range(level_length):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            averages.append(level_sum / level_length)

        return averages
