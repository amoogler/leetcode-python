class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1))
        R, C = len(grid), len(grid[0])
        queue = deque([])

        if grid[0][0] == 0:
            queue.append((0, 0))

        while queue:
            r, c = queue.popleft()

            if r == R - 1 and c == C - 1:
                return grid[r][c] + 1

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                    queue.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1

        return -1
