class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        self.DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        self.grid = grid
        borders, islands = deque([]), deque([])
        count = 0

        for i, j in product(range(self.R), range(self.C)):
            if (i == 0 or i == self.R - 1 or j == 0 or j == self.C - 1) and grid[i][j] == 0:
                borders.append((i, j))

        # Mark escaped '0' as '1'.
        self.bfs(borders)

        # Now, question becomes how many islands in the grid.
        for i, j in product(range(1, self.R - 1), range(1, self.C - 1)):
            if grid[i][j] == 0:
                islands.append((i, j))
                self.bfs(islands)
                count += 1

        return count

    def bfs(self, queue: deque):
        while queue:
            r, c  = queue.popleft()
            self.grid[r][c] = 1

            for dr, dc in self.DIRS:
                nr, nc = r + dr, c + dc

                if 0 <= nr < self.R and 0 <= nc < self.C and self.grid[nr][nc] == 0:
                    queue.append((nr, nc))
