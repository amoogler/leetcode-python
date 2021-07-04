# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         count = 0

#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     count += 1

#                 self.dfs(grid, i, j)

#         return count

#     def dfs(self, grid: List[List[str]], row: int, col: int) -> None:
#         if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
#             return

#         if grid[row][col] != '1':
#             return

#         grid[row][col] = '0'

#         DIR = ((1, 0), (-1, 0), (0, 1), (0, -1))

#         for dr, dc in DIR:
#             self.dfs(grid, row + dr, col + dc)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        self.DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        count = 0

        for i in range(self.R):
            for j in range(self.C):
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
                new_r, new_c = r + dr, c + dc

                if new_r < 0 or new_r >= self.R or new_c < 0 or new_c >= self.C:
                    continue

                if grid[new_r][new_c] != '1':
                    continue

                queue.append((new_r, new_c))
                grid[new_r][new_c] = '0'
