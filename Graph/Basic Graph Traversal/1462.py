class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = []
        self.graph = defaultdict(list)

        # Build an adjacency list to represent graph.
        for a, b in prerequisites:
            self.graph[a].append(b)

        for u, v in queries:
            ans.append(self.isPrerequisites(u, v))

        return ans

    # BFS Solution.
    def isPrerequisites(self, start: int, end: int) -> bool:
        queue = deque([start])
        seen = set()

        while queue:
            curr = queue.popleft()

            if curr == end:
                return True

            for v in self.graph[curr]:
                if v not in seen:
                    queue.append(v)
                    seen.add(v)

        return False

    # DFS Solution
    # Time Limited Exceeded.
    def isPrerequisites(self, start: int, end: int) -> bool:
        visited = set()

        # Memoization
        @lru_cache
        def dfs(start, end):
            if start == end:
                return True

            if start in visited:
                return False

            visited.add(start)

            for v in self.graph[start]:
                if self.isPrerequisites(v, end):
                    return True

            return False

        return dfs(start, end)
