# This problem a graph-based equavalent of LC-200 Number_Of_Islands.

# BFS Soluting using Adjacency Matrix.
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph, visited = [[0] * n for _ in range(n)], [0] * n
        queue = deque()
        count = 0

        for a, b in edges:
            graph[a][b] = 1
            graph[b][a] = 1

        for i in range(n):
            if visited[i]:
                continue

            queue.append(i)

            while queue:
                node = queue.popleft()
                visited[node] = 1

                for j in range(n):
                    if graph[node][j] == 1 and visited[j] == 0:
                        queue.append(j)

            count += 1

        return count

# BFS Solution using Adjacency List.
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph, visited, queue = defaultdict(list), [0] * n, deque()
        count = 0

        # Build an adjacency list to represent an undirected graph.
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for i in range(n):
            if visited[i]:
                continue

            queue.append(i)

            while queue:
                node = queue.popleft()
                visited[node] = 1

                for v in graph[node]:
                    if not visited[v]:
                        queue.append(v)

            count += 1

        return count

# DFS Solution using Adjacency List.
class Solution:
    def dfs(self, node: int):
        if node in self.visited:
            return

        self.visited.add(node)

        for neighbor in self.graph[node]:
            self.dfs(neighbor)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.graph, self.visited = defaultdict(list), set()
        count = 0

        # Build an adjacency list to represent an undirected graph.
        for a, b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)

        for i in range(n):
            if i not in self.visited:
                self.dfs(i)
                count += 1

        return count
