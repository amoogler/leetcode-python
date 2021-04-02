from typing import List
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = []
        
        if not root:
            return levels
        
        queue = deque([root])
        prev, curr, level = 1, 0, []
        
        while queue:
            node = queue.popleft()
            prev -= 1
            level.append(node.val)
            
            for child in node.children:
                if child:
                    queue.append(child)
                    curr += 1
            
            if prev == 0:
                levels.append(level)
                level = []
                prev = curr
                curr = 0
        
        return levels