class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = deque([])
        fresh_oranges = 0

        # Find all the rotten oranges.
        for i, j in product(range(R), range(C)):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_oranges += 1

        if fresh_oranges == 0:
            return 0

        minute = 0
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                r, c = queue.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        queue.append((nr, nc))

            minute += 1

        return minute - 1 if fresh_oranges == 0 else -1
