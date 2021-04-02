from typing import List
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        
        if not root:
            return levels

        queue = deque([root])
        prev = 1
        curr = 0
        level = []
        
        while queue:
            node = queue.popleft()
            level.append(node.val)
            prev -= 1
            
            if node.left:
                queue.append(node.left)
                curr += 1
            
            if node.right:
                queue.append(node.right)
                curr += 1

            if prev == 0:
                levels.append(level)
                level = []
                prev = curr
                curr = 0

        return levels
