# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        node_values = set()
        queue = collections.deque([root])

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                node = queue.popleft()
                node_values.add(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        min_value, ans = root.val, float('inf')

        for node_value in node_values:
            if min_value < node_value < ans:
                ans = node_value

        return ans if ans < float('inf') else -1
