from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_sums = []
        queue = deque([root])
        
        while queue:
            level_sum = 0
            level_length = len(queue)
            
            while level_length > 0:
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                level_length -= 1

            level_sums.append(level_sum)
            level_sum = 0

        min_level = 0
        max_sum = max(level_sums)

        for idx, level_sum in enumerate(level_sums):
            if level_sum == max_sum:
                min_level = idx + 1
                break
        
        return min_level
