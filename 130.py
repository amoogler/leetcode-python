# BFS Solution:
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.R, self.C = len(board), len(board[0])
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        borders = deque([])

        # Find all the 'O' grids on 4 borders.
        for i, j in product(range(self.R), range(self.C)):
            if i == 0 or i == self.R - 1 or j == 0 or j == self.C - 1:
                if board[i][j] == 'O':
                    borders.append((i, j))

        def bfs(queue: deque):
            DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
            seen = set()

            for r, c in queue:
                seen.add((r, c))

            while queue:
                r, c  = queue.popleft()

                if board[r][c] != 'O':
                    continue

                board[r][c] = 'E'

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < self.R and 0 <= nc < self.C and (nr, nc) not in seen:
                        queue.append((nr, nc))
                        seen.add((nr, nc))

        # Mark escaped grids with 'E'.
        bfs(borders)

        # Flip captured grids from 'O' -> 'X', and escaped ones from 'E' -> 'O'.
        for i, j in product(range(self.R), range(self.C)):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'E':
                board[i][j] = 'O'

# DFS Solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.R, self.C = len(board), len(board[0])
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        borders = deque([])

        # Find all the 'O' grids on 4 borders.
        for i, j in product(range(self.R), range(self.C)):
            if i == 0 or i == self.R - 1 or j == 0 or j == self.C - 1:
                if board[i][j] == 'O':
                    self.dfs(board, i, j)

        # Flip captured grids from 'O' -> 'X', and escaped ones from 'E' -> 'O'.
        for i, j in product(range(self.R), range(self.C)):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'E':
                board[i][j] = 'O'

    def dfs(self, board: List[List[str]], row: int, col: int):
        if not (0 <= row < self.R and 0 <= col < self.C):
            return

        if board[row][col] != 'O':
            return

        board[row][col] = 'E'

        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dr, dc in DIRS:
            self.dfs(board, row + dr, col + dc)
