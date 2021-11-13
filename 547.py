# This problem is to find number of connected component in an un-directed graph.

# BFS Iterative Solution
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = [0] * N
        queue = deque()
        count = 0

        for i in range(N):
            if not visited[i]:
                queue.append(i)

                while queue:
                    node = queue.popleft()
                    visited[node] = 1

                    for j in range(N):
                        if isConnected[node][j] == 1 and visited[j] == 0:
                            queue.append(j)

                count += 1

        return count

# DFS Recursive Solution
class Solution:
    def dfs(self, isConnected: List[List[int]], visited: List[int], i: int) -> None:
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(isConnected, visited, j)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = [0] * N
        count = 0

        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                self.dfs(isConnected, visited, i)
                count += 1

        return count
