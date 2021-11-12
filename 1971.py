# BFS Solution
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        seen, graph = set(), defaultdict(list)

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        queue = deque([start])
        seen.add(start)

        while queue:
            curr = queue.popleft()

            if curr == end:
                return True

            for v in graph[curr]:
                if v not in seen:
                    queue.append(v)
                    seen.add(v)

        return False

# DFS Solution
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        visited, graph = set(), defaultdict(list)

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        def dfs(node, end):
            if node == end:
                return True

            if node in visited:
                return False

            visited.add(node)

            for v in graph[node]:
                if dfs(v, end):
                    return True

            return False

        return dfs(start, end)
