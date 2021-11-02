class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                value = board[r][c]

                if value == '.':
                    continue

                if value in rows[r]:
                    return False
                rows[r].add(value)

                if value in cols[c]:
                    return False
                cols[c].add(value)

                idx = (r // 3) * 3 + c // 3
                if value in boxes[idx]:
                    return False
                boxes[idx].add(value)

        return True
