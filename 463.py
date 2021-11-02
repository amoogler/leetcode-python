class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        perimeter = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        perimeter += 1

                    if i + 1 >= R or grid[i + 1][j] == 0:
                        perimeter += 1

                    if j - 1 < 0 or grid[i][j - 1] == 0:
                        perimeter += 1

                    if j + 1 >= C or grid[i][j + 1] == 0:
                        perimeter += 1

        return perimeter
