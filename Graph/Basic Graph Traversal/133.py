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

        graph = {}
        queue = deque([node])
        graph[node] = Node(node.val, [])

        while queue:
            n = queue.popleft()

            for neighbor in n.neighbors:
                if neighbor not in graph:
                    graph[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)

                graph[n].neighbors.append(graph[neighbor])

        return graph[node]

# DFS Recursive Solution
class Solution:
    def __init__(self):
        self.graph = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        if node in self.graph:
            return self.graph[node]

        clone_node = Node(node.val, [])
        self.graph[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node
