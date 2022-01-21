# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# Level-order traversal, after the first NULL node,
# there should be no non-NULL node left in the queue.
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                break

            queue.append(node.left)
            queue.append(node.right)

        while queue:
            node = queue.popleft()

            if node:
                return False

        return True
