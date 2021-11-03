class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        R, C = len(grid), len(grid[0])
        perimeter = 0

        for r, c in product(range(R), range(C)):
            if grid[r][c] == 0:
                continue

            for dr, dc in DIRS:
                nx, ny = r + dr, c + dc

                if not (0 <= nx < R and 0 <= ny < C):
                    perimeter += 1
                elif grid[nx][ny] == 0:
                    perimeter += 1

        return perimeter
