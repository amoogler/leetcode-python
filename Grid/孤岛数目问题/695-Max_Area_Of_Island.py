from typing import List
from collections import deque

# DFS Solution.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_size = max(self.computeIslandSize(grid, i, j), max_size)

        return max_size

    def computeIslandSize(self, grid: List[List[int]], row: int, col: int) -> int:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0

        if grid[row][col] != 1:
            return 0

        grid[row][col] = 0

        island_size = 0
        DIR = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for dr, dc in DIR:
            island_size += self.computeIslandSize(grid, row + dr, col + dc)

        return 1 + island_size

# BFS Solution.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.R, self.C = len(grid), len(grid[0])

        for i, j in product(range(self.R), range(self.C)):
            if grid[i][j] == 1:
                grid[i][j] = 0
                area = self.computeArea(grid, i, j)
                max_area = max(area, max_area)
        
        return max_area
    
    def computeArea(self, grid: List[List[int]], row: int, col: int) -> int:
        queue = deque([(row, col)])
        DIRS = ((-1, 0), (0, -1), (1, 0), (0, 1))
        area = 1

        while queue:
            r, c = queue.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < self.R and 0 <= nc < self.C and grid[nr][nc] == 1):
                    continue
                
                grid[nr][nc] = 0
                area += 1
                queue.append((nr, nc))
        
        return area
