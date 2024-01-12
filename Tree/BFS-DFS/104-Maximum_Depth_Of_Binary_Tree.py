# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS recursive solution.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
 
# BFS solution.
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 0
        queue = deque([root])

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth
