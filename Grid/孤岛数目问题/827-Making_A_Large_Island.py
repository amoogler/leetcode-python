# DFS Solution.
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        indexToArea = dict()
        self.R, self.C = len(grid), len(grid[0])
        self.DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        max_area = 0
        flag = -1

        # Pick an identifier index for each connected component
        # and build a map for identifier to area.
        for i in range(self.R):
            for j in range(self.C):
                if grid[i][j] == 1:
                    area = [0]
                    self.dfs(grid, i, j, area, flag)
                    indexToArea[flag] = area[0]
                    max_area = max(max_area, area[0])
                    flag -= 1

        # At each '0' and check its neighbor connected components,
        # then come up with new area.
        for i in range(self.R):
            for j in range(self.C):
                if grid[i][j] == 0:
                    area = self.getNeighbors(grid, i, j, indexToArea)
                    max_area = max(max_area, area)

        return max_area

    def dfs(self, grid: List[List[int]], row: int, col: int, area: List[int], flag: int):
        if not (0 <= row < self.R and 0 <= col < self.C and grid[row][col] == 1):
            return

        area[0] += 1
        grid[row][col] = flag

        for dr, dc in self.DIRS:
            self.dfs(grid, row + dr, col + dc, area, flag)

    def getNeighbors(self, grid: List[List[int]], row: int, col: int, indexToArea: dict) -> int:
        new_area = 0
        checked = set()

        for dr, dc in self.DIRS:
            nr, nc = row + dr, col + dc

            if not (0 <= nr < self.R and 0 <= nc < self.C):
                continue

            neighbor = grid[nr][nc]

            if neighbor == 0 or neighbor in checked:
                continue

            new_area += indexToArea[neighbor]
            checked.add(neighbor)

        return new_area + 1
