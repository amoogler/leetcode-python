class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        DIRS = ((-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1))
        queue = deque([(0, 0)])
        seen = set()
        seen.add((0, 0))
        steps = 0

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                r, c = queue.popleft()

                if (r, c) == (x, y):
                    return steps

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if (nr, nc) in seen:
                        continue

                    seen.add((nr, nc))
                    queue.append((nr, nc))

            steps += 1

        return -1
