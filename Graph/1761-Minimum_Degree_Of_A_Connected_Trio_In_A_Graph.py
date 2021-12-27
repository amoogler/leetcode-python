# Solution results in TLE using adjacency list.
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        degree = [0] * (n + 1)
        res = float('inf')

        # Build an adjacency list to represent the undirected graph.
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u] += 1
            degree[v] += 1

        for x in range(1, n + 1):
            for y in graph[x]:
                for z in graph[x]:
                    if y >= z or z not in graph[y]:
                        continue

                    res = min(res, degree[x] + degree[y] + degree[z] - 6)

        return res if res < float('inf') else -1

# Solution passed using adjacency matrix.
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        degree = [0] * (n + 1)
        res = float('inf')

        # Build an adjacency matrix to represent the undirected graph.
        graph = [[False] * (n + 1) for _ in range(n + 1)]

        for u, v in edges:
            graph[u][v] = True
            graph[v][u] = True
            degree[u] += 1
            degree[v] += 1

        for x in range(1, n + 1):
            for y in range(x + 1, n + 1):
                if graph[x][y]:
                    for z in range(y + 1, n + 1):
                        if graph[x][z] and graph[y][z]:
                            res = min(res, degree[x] + degree[y] + degree[z] - 6)

        return res if res < float('inf') else -1
