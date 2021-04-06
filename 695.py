class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_size = max(self.computeIslandSize(grid, i, j), max_size)

        return max_size

    def computeIslandSize(self, grid: List[List[int]], row: int, col: int) -> int:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
            return 0

        grid[row][col] = 0

        island_size = 0
        island_size += self.computeIslandSize(grid, row + 1, col)
        island_size += self.computeIslandSize(grid, row - 1, col)
        island_size += self.computeIslandSize(grid, row, col + 1)
        island_size += self.computeIslandSize(grid, row, col - 1)

        return 1 + island_size
