from typing import List
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        right_nodes = []
        
        if not root:
            return right_nodes
        
        queue = deque([root])
        
        while queue:
            level_length = len(queue)
            
            while level_length > 0:
                node = queue.popleft()
                
                if level_length == 1:
                    right_nodes.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
                level_length -= 1

        return right_nodes
