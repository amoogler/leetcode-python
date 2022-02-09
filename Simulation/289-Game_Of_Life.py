# Rules:
# 0. 1 represents alive, 0 represents dead.
# 1. < 2 neighbors are alive or > 3 neighbors are alive, alive -> dead.
# 2. 2, 3 neighbors are alive, live on.
# 3. 3 neighbors are alive, dead -> alive.

# Time complexity = O(nm), Space complexity = O(nm)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1))
        R, C = len(board), len(board[0])
        new_board = [[0] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                count = 0

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < R and 0 <= nc < C):
                        continue

                    if board[nr][nc] == 1:
                        count += 1

                if board[r][c] == 1 and (count == 2 or count == 3):
                    new_board[r][c] = 1
                elif board[r][c] == 0 and count == 3:
                    new_board[r][c] = 1

        for r in range(R):
            for c in range(C):
                board[r][c] = new_board[r][c]

# Time complexity = O(nm), Space complexity = O(1)
# -1 -> alive to dead
# 2 -> dead to alive
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1))
        R, C = len(board), len(board[0])

        for r in range(R):
            for c in range(C):
                count = 0

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < R and 0 <= nc < C):
                        continue

                    if board[nr][nc] == 1 or board[nr][nc] == -1:
                        count += 1

                if board[r][c] == 1 and (count < 2 or count > 3):
                    board[r][c] = -1
                elif board[r][c] == 0 and count == 3:
                    board[r][c] = 2

        for r in range(R):
            for c in range(C):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1

# Follow-up: Infinitely large board.
# 1. Impossible to iterate a matrix that large.
# 2. Impossible to store large board in memory.
# 3. For super sparse matrix, we waste a lot of space to store the huge board.
# e.g. a gigantic matrix with a very few live cells.
#
# It would make sense to actually save the location of only live cells and apply rules.
# 1. mmap() read file directly
# 2. Streaming the data from file. Only load 3 rows at a time because we don't need the neighbors.
