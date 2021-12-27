class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = len(board)
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(N):
            for c in range(N):
                v = board[r][c]

                if v == '.':
                    continue

                rows[r].add(v)
                cols[c].add(v)
                boxes[(r // 3) * 3 + c // 3].add(v)

        def is_valid(row: int, col: int, value: str) -> bool:
            box_id = (row // 3) * 3 + col // 3
            return value not in rows[row] and value not in cols[col] and value not in boxes[box_id]

        def backtrack(board: List[List[int]]) -> bool:
            for r in range(N):
                for c in range(N):
                    if board[r][c] != '.':
                        continue

                    for i in range(ord('1'), ord('9') + 1):
                        v = chr(i)
                        if is_valid(r, c, v):
                            board[r][c] = v
                            rows[r].add(v)
                            cols[c].add(v)
                            boxes[(r // 3) * 3 + c // 3].add(v)

                            if backtrack(board):
                                return True

                            # Backtracking.
                            board[r][c] = '.'
                            rows[r].remove(v)
                            cols[c].remove(v)
                            boxes[(r // 3) * 3 + c // 3].remove(v)

                    return False
            return True

        backtrack(board)
