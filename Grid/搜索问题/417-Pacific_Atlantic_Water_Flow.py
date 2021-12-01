class Solution:
    DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.R, self.C = len(heights), len(heights[0])
        self.heights = heights
        res = []

        pacific_queue = deque([])
        atlantic_queue = deque([])
        pacific_seen = set()
        atlantic_seen = set()

        for i in range(self.R):
            pacific_queue.append((i, 0))
            pacific_seen.add((i, 0))
            atlantic_queue.append((i, self.C - 1))
            atlantic_seen.add((i, self.C - 1))

        for i in range(self.C):
            pacific_queue.append((0, i))
            pacific_seen.add((0, i))
            atlantic_queue.append((self.R - 1, i))
            atlantic_seen.add((self.R - 1, i))

        self.bfs(pacific_queue, pacific_seen)
        self.bfs(atlantic_queue, atlantic_seen)

        for i in range(self.R):
            for j in range(self.C):
                if (i, j) in pacific_seen and (i, j) in atlantic_seen:
                    res.append((i, j))

        return res

    def bfs(self, queue: Deque, seen: set) -> None:

        while queue:
            row, col = queue.popleft()

            for dr, dc in self.DIRS:
                nr, nc = row + dr, col + dc

                if 0 <= nr < self.R and 0 <= nc < self.C and \
                    (nr, nc) not in seen and \
                    self.heights[nr][nc] >= self.heights[row][col]:

                    queue.append((nr, nc))
                    seen.add((nr, nc))
