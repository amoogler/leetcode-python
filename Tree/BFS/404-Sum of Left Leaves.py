# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum_left = 0
        if not root:
            return sum_left
        
        queue = deque([root])
        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                if not node.left.left and not node.left.right:
                    sum_left += node.left.val
            if node.right:
                queue.append(node.right)

        return sum_left
