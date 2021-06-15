class Solution:
    DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.R, self.C = len(heights), len(heights[0])
        res = []

        pacific_queue = deque([])
        atlantic_queue = deque([])

        for i in range(self.R):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, self.C -1))

        for i in range(self.C):
            pacific_queue.append((0, i))
            atlantic_queue.append((self.R - 1, i))

        pacific_visited = self.bfs(pacific_queue, heights)
        allantic_visited = self.bfs(atlantic_queue, heights)

        for i in range(self.R):
            for j in range(self.C):
                if pacific_visited[i][j] and allantic_visited[i][j]:
                    res.append((i, j))

        return res

    def bfs(self, queue: Deque, heights: List[List[int]]):
        visited = [[False] * self.C for _ in range(self.R)]

        while queue:
            row, col = queue.popleft()
            visited[row][col] = True

            for dr, dc in self.DIRS:
                new_row, new_col = row + dr, col + dc

                if new_row < 0 or new_row >= self.R or new_col < 0 or new_col >= self.C:
                    continue

                if visited[new_row][new_col]:
                    continue

                if heights[new_row][new_col] < heights[row][col]:
                    continue

                queue.append((new_row, new_col))

        return visited
