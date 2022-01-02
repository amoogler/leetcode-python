# This problem is to find number of connected component in an un-directed graph.
# This problem is a graph version of LC-200.

# BFS Iterative Solution
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.N = len(isConnected)
        seen = set()
        count = 0

        for i in range(self.N):
            if i not in seen:
                count += 1
                seen.add(i)
                self.bfs(seen, i, isConnected)

        return count

    def bfs(self, seen: set, pos: int, isConnected: List[List[int]]) -> None:
        queue = deque([pos])

        while queue:
            node = queue.popleft()

            for j in range(self.N):
                if isConnected[node][j] == 1 and j not in seen:
                    queue.append(j)
                    seen.add(j)

# DFS Recursive Solution
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.N = len(isConnected)
        seen = set()
        count = 0

        for i in range(self.N):
            if i not in seen:
                count += 1
                self.dfs(seen, i, isConnected)

        return count

    def dfs(self, seen: set, pos: int, isConnected: List[List[int]]) -> None:
        if pos in seen:
            return

        seen.add(pos)

        for j in range(self.N):
            if isConnected[pos][j] == 1:
                self.dfs(seen, j, isConnected)
