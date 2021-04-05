# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = collections.deque([(root, None)])
        
        while queue:
            level = {}
            level_length = len(queue)
            
            for _ in range(level_length):
                node, parent = queue.popleft()
                level[node.val] = parent
                
                if node.left:
                    queue.append((node.left, node.val))
                
                if node.right:
                    queue.append((node.right, node.val))

            if x in level and y in level:
                return level[x] != level[y]
              
        return False
