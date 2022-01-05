# This is a grid-based (i.e. graph-based) problem, asking shortest path.
# We can solve it using BFS.

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        OBS = 1
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = deque([(0, 0, k)])
        seen = set()
        seen.add((0, 0, k))
        distance = 0

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                r, c, curr_k = queue.popleft()

                if (r, c) == (R - 1, C - 1):
                    return distance

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < R and 0 <= nc < C):
                        continue

                    if grid[nr][nc] == OBS:
                        if curr_k == 0:
                            continue

                        if (nr, nc, curr_k - 1) in seen:
                            continue

                        queue.append((nr, nc, curr_k - 1))
                        seen.add((nr, nc, curr_k - 1))
                    else:
                        if (nr, nc, curr_k) in seen:
                            continue

                        queue.append((nr, nc, curr_k))
                        seen.add((nr, nc, curr_k))

            distance += 1

        return -1
