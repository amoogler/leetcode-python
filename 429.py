from typing import List

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
        
        queue = collections.deque([root])
        
        while queue:
            level = []
            level_length = len(queue)
            
            for _ in range(level_length):
                node = queue.popleft()
                level.append(node.val)
            
                for child in node.children:
                    if child:
                        queue.append(child)

            levels.append(level)
        
        return levels
