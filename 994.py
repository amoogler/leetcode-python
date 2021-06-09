class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = deque([])
        fresh_oranges = 0

        # Find all the rotten oranges.
        for i in range(R):
            for j in range(C):
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
                    new_r, new_c = r + dr, c + dc

                    if new_r < 0 or new_r >= R or new_c < 0 or new_c >= C or \
                        grid[new_r][new_c] != 1:
                        continue

                    grid[new_r][new_c] = 2
                    fresh_oranges -= 1
                    queue.append((new_r, new_c))

            minute += 1

        return minute - 1 if fresh_oranges == 0 else -1
