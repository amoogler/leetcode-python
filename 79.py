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

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        if board[row][col] != word[idx]:
            return False

        res = False
        temp = board[row][col]
        board[row][col] = ''
        DIR = ((1, 0), (-1, 0), (0, 1), (0, -1))

        if any(self.dfs(board, row + dr, col + dc, word, idx + 1) for dr, dc in DIR):
            res = True

        board[row][col] = temp
        return res
