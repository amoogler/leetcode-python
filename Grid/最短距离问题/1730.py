# BFS Solution, search starts from '*'
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        self.FOOD, self.SPACE, self.PERSON = '#', 'O', '*'
        distance = 0

        for i, j in product(range(self.R), range(self.C)):
            if grid[i][j] == self.PERSON:
                grid[i][j] = 0
                distance = self.bfs(grid, i, j)

        return distance

    def bfs(self, grid: List[List[str]], row: int, col: int) -> int:
        queue = deque([(row, col)])
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            r, c = queue.popleft()

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < self.R and 0 <= nc < self.C):
                    continue

                if grid[nr][nc] == self.FOOD:
                    return grid[r][c] + 1

                if grid[nr][nc] == self.SPACE:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))

        return -1

# BFS Solution, search starts from food '#'.
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        self.FOOD, self.SPACE, self.PERSON = '#', 'O', '*'
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        queue = deque([])

        for i, j in product(range(self.R), range(self.C)):
            if grid[i][j] == self.FOOD:
                grid[i][j] = 0
                queue.append((i, j))

        while queue:
            r, c = queue.popleft()

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < self.R and 0 <= nc < self.C):
                    continue

                if grid[nr][nc] == self.PERSON:
                    return grid[r][c] + 1

                if grid[nr][nc] == self.SPACE:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))

        return -1
