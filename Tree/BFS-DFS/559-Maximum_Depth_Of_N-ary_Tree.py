"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# DFS recursive solution.
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        if all(not child for child in root.children):
            return 1

        max_depth = 0

        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))

        return max_depth + 1


# BFS solution.
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0

        if not root:
            return max_depth

        queue = deque([root])

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                node = queue.popleft()

                for child in node.children:
                    if child:
                        queue.append(child)

            max_depth += 1

        return max_depth

