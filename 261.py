# 1. Graph is fully connected. i.e. for every pair of vertices, there is a path between them.
# 2. Graph contains no cycles. i.e. there is exactly one path between two vertices in the graph.

# DFS Iterative Solution
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = defaultdict(list)

        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        stack = [0]
        parent = {0: -1}

        while stack:
            node = stack.pop()

            for neighbor in adjacency[node]:
                if parent[node] == neighbor:
                    continue

                if neighbor in parent:
                    return False

                stack.append(neighbor)
                parent[neighbor] = node

        return len(parent) == n

# Iterative BFS Solution
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = defaultdict(list)

        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        parent = {0: -1}
        queue = deque([0])

        while queue:
            node = queue.popleft()

            for neighbor in adjacency[node]:
                if parent[node] == neighbor:
                    continue

                if neighbor in parent:
                    return False

                queue.append(neighbor)
                parent[neighbor] = node

        return len(parent) == n

# DFS Recursive Solution
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = defaultdict(list)

        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adjacency[node]:
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
