class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count, row, col = 0, len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0 and self.isClosedIsland(grid, i, j):
                    count += 1
        return count

    def isClosedIsland(self, grid: List[List[int]], i: int, j: int) -> bool:
        is_closed, row, col = True, len(grid), len(grid[0])

        if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != 0:
            return is_closed
        elif grid[i][j] == 0:
            grid[i][j] = 1

            border = i == 0 or i == row - 1 or j == 0 or j == col - 1
            is_closed &= not border

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for a, b in directions:
                is_closed &= self.isClosedIsland(grid, i + a, j + b)

        return is_closed
