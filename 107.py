from typing import List
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []

        if not root:
            return levels
        
        queue = deque([root])
        
        while queue:
            level = []
            level_length = len(queue)
            
            for _ in range(level_length):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            levels.append(level)
        
        return reversed(levels)
