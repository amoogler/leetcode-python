class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        self.queue = deque([])
        self.DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        self.visited = set()

        # Mark island1 to all 0s.
        for i, j in product(range(self.R), range(self.C)):
            if grid[i][j] == 1:
                grid[i][j] = 0
                self.queue.append((i, j))
                self.markIsland(grid, i, j, 0)
                break

        # Mark island2 to all 'x'.
        for i, j in product(range(self.R), range(self.C)):
            if grid[i][j] == 1:
                grid[i][j] = 'x'
                self.markIsland(grid, i, j, 'x')
                break

        # From all nodes in island1, search for island2 using BFS.
        while self.queue:
            r, c = self.queue.popleft()
            self.visited.add((r, c))

            for dr, dc in self.DIRS:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < self.R and 0 <= nc < self.C and (nr, nc) not in self.visited):
                    continue

                if grid[nr][nc] == 0:
                    grid[nr][nc] = grid[r][c] + 1
                    self.queue.append((nr, nc))
                elif grid[nr][nc] == 'x':
                    return grid[r][c]

    def markIsland(self, grid, row, col, mark) -> None:
        helper_queue = deque([(row, col)])

        while helper_queue:
            r, c = helper_queue.popleft()

            for dr, dc in self.DIRS:
                nr, nc = r + dr, c + dc

                if 0 <= nr < self.R and 0 <= nc < self.C and grid[nr][nc] == 1:
                    helper_queue.append((nr, nc))
                    grid[nr][nc] = mark

                    if mark == 0:
                        self.queue.append((nr, nc))
                        self.visited.add((nr, nc))
