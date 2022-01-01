# DFS Solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        count = 0

        for i, j in product(range(self.R), range(self.C)):
            if grid[i][j] == '1':
                count += 1
                self.dfs(grid, i, j)

        return count

    def dfs(self, grid: List[List[str]], row: int, col: int) -> None:
        if not (0 <= row < self.R and 0 <= col < self.C and grid[row][col] == '1'):
            return

        grid[row][col] = '0'

        DIR = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dr, dc in DIR:
            self.dfs(grid, row + dr, col + dc)

# BFS Solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        self.DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        count = 0

        for i, j in product(range(self.R), range(self.C)):
            if grid[i][j] == '1':
                count += 1
                grid[i][j] = '0'
                self.bfs(grid, i, j)

        return count

    def bfs(self, grid: List[List[str]], row: int, col: int) -> int:
        queue = deque([(row, col)])

        while queue:
            r, c = queue.popleft()

            for dr, dc in self.DIRS:
                nr, nc = r + dr, c + dc

                if 0 <= nr < self.R and 0 <= nc < self.C and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'
