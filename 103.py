from typing import List
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        
        if not root:
            return levels
        
        queue = deque([root])
        toggle = False
        
        while queue:
            level = []
            level_length = len(queue)
            
            while level_length > 0:
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
                level_length -= 1
            
            if (toggle):
                levels.append(reversed(level))
            else:
                levels.append(level)
        
            level = []
            toggle = not toggle

        return levels               
