from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0
        
        if not root:
            return max_depth
        
        queue = deque([root])
        
        while queue:
            queue_length = len(queue)
            
            while queue_length > 0:
                node = queue.popleft()
                
                for child in node.children:
                    if child:
                        queue.append(child)
                        
                queue_length -= 1
                  
            max_depth += 1
        
        return max_depth
