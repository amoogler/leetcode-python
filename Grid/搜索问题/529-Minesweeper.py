class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click[0], click[1]

        if not board:
            return board

        # Game over upon mine is revealed.
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board

        # Recusively reveal the board.
        self.revealBoard(board, row, col)
        return board

    def revealBoard(self, board: List[List[str]], r: int, c: int) -> None:
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        R, C = len(board), len(board[0])
        mine_count = 0

        # Base case.
        if not (0 <= r < R and 0 <= c < C):
            return

        if board[r][c] != 'E':
            return

        for dr, dc, in DIRS:
            nr, nc = r + dr, c + dc

            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 'M':
                mine_count += 1

        if mine_count == 0:
            board[r][c] = 'B'
        else:
            board[r][c] = str(mine_count)
            return

        # Recursive steps.
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            self.revealBoard(board, nr, nc)
