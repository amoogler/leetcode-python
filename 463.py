class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        perimeter = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    if i - 1 < 0 or (i - 1 >= 0 and grid[i - 1][j]) == 0:
                        perimeter += 1

                    if i + 1 >= R or (i + 1 < R and grid[i + 1][j]) == 0:
                        perimeter += 1

                    if j - 1 < 0 or (j - 1 >= 0 and grid[i][j - 1] == 0):
                        perimeter += 1

                    if j + 1 >= C or (j + 1 < C and grid[i][j + 1] == 0):
                        perimeter += 1

        return perimeter
