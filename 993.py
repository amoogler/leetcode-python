# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = collections.deque([root])
        
        while queue:
            level = set()
            level_length = len(queue)
            
            for _ in range(level_length):
                node = queue.popleft()
                level.add(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                if not node.left or not node.right:
                    continue

                # Siblings
                if (x == node.left.val and y == node.right.val) or \
                   (x == node.right.val and y == node.left.val):
                    return False

            if x in level and y in level:
                return True
              
        return False
