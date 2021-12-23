class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Build an adjacency list to represent an undirected graph.
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node: int) -> int:
            if node in visited:
                return 0

            visited.add(node)
            seconds = 0

            for child in graph[node]:
                seconds += dfs(child)

            if seconds > 0:
                return seconds + 2

            return 2 if hasApple[node] else 0

        return max(dfs(0) - 2, 0)
