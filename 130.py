class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.R, self.C = len(board), len(board[0])
        borders = []

        # Find all the 'O' grids on 4 borders.
        for i in range(self.R):
            if board[i][0] == 'O':
                borders.append((i, 0))

            if board[i][self.C - 1] == 'O':
                borders.append((i, self.C - 1))

        for i in range(self.C):
            if board[0][i] == 'O':
                borders.append((0, i))

            if board[self.R - 1][i] == 'O':
                borders.append((self.R - 1, i))

        # Mark escaped grids with 'E'.
        for r, c in borders:
            self.bfs(board, r, c)

        # Flip captured grids from 'O' -> 'X', and escaped ones from 'E' -> 'O'.
        for i in range(self.R):
            for j in range(self.C):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'

#     def dfs(self, board: List[List[str]], row: int, col: int):
#         if row < 0 or row >= self.R or col < 0 or col >= self.C:
#             return

#         if board[row][col] != 'O':
#             return

#         board[row][col] = 'E'
#         DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

#         for dr, dc in DIRS:
#             self.dfs(board, row + dr, col + dc)

    def bfs(self, board: List[List[str]], row: int, col: int):
        queue = deque([(row, col)])
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            r, c  = queue.popleft()

            if board[r][c] != 'O':
                continue

            board[r][c] = 'E'

            for dr, dc in DIRS:
                new_r, new_c = r + dr, c + dc

                if new_r >= 0 and new_r < self.R and new_c >= 0 and new_c < self.C:
                    queue.append((new_r, new_c))
