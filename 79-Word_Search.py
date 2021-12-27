class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True

        return False

    def dfs(self, board: List[List[str]], row: int, col: int, word: str, idx: int) -> bool:
        if idx == len(word):
            return True

        if not (0 <= row < len(board) and 0 <= col < len(board[0])):
            return False

        if board[row][col] != word[idx]:
            return False

        board[row][col] = '#'
        DIR = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for dr, dc in DIR:
            if self.dfs(board, row + dr, col + dc, word, idx + 1):
                return True

        board[row][col] = word[idx]
        return False
