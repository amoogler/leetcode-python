from typing import List

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
        
        queue = collections.deque([root])
        toggle = False
        
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
            
            if (toggle):
                levels.append(reversed(level))
            else:
                levels.append(level)

            toggle = not toggle

        return levels               
