class Solution:
    DIRS = {
        (1, 0) : 'D',
        (-1, 0): 'U',
        (0, 1) : 'R',
        (0, -1): 'L'
    }

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        distinct_islands = set()

        for i in range(self.R):
            for j in range(self.C):
                if grid[i][j] == 1:
                    island = self.bfs(grid, i, j)
                    distinct_islands.add(island)

        return len(distinct_islands)

    def bfs(self, grid: List[List[int]], row: int, col: int):
        queue = deque([(row, col)])
        island = []

        while queue:
            r, c = queue.popleft()
            grid[r][c] = 0

            for (dr, dc), dv in self.DIRS.items():
                new_r, new_c = r + dr, c + dc

                if new_r < 0 or new_r >= self.R or new_c < 0 or new_c >= self.C:
                    island.append('Q')
                    continue

                if grid[new_r][new_c] != 1:
                    island.append('Q')
                    continue

                island.append(dv)
                grid[new_r][new_c] = 0
                queue.append((new_r, new_c))

        return ''.join(island)
