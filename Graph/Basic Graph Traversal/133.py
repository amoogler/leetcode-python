"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# BFS Solution
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        # A map from original node to its clone.
        clone = {}
        queue = deque([node])
        clone[node] = Node(node.val, [])

        while queue:
            n = queue.popleft()

            for neighbor in n.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)

                clone[n].neighbors.append(clone[neighbor])

        return clone[node]

# DFS Recursive Solution
class Solution:
    def __init__(self):
        self.clone = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        if node in self.clone:
            return self.clone[node]

        clone_node = Node(node.val, [])
        self.clone[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node
