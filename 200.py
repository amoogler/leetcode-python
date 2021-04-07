class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1

                self.dfs(grid, i, j)

        return count

    def dfs(self, grid: List[List[str]], row: int, col: int) -> None:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return

        if grid[row][col] != '1':
            return

        grid[row][col] = '0'

        DIR = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for dr, dc in DIR:
            self.dfs(grid, row + dr, col + dc)
