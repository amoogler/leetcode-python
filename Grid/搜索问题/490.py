class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        R, C = len(maze), len(maze[0])
        seen = set()
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        queue = deque([start])
        seen.add((start[0], start[1]))
        EMPTY = 0

        while queue:
            r, c = queue.popleft()

            if r == destination[0] and c == destination[1]:
                return True

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                while 0 <= nr < R and 0 <= nc < C and maze[nr][nc] == EMPTY:
                    nr += dr
                    nc += dc

                if (nr - dr, nc - dc) not in seen:
                    queue.append([nr - dr, nc - dc])
                    seen.add((nr - dr, nc - dc))

        return False
