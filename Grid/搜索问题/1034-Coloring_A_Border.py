class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        selected_color = grid[row][col]
        queue = deque([(row, col)])
        seen = {(row, col)}
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while queue:
            r, c = queue.popleft()
            is_border = False

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if (nr, nc) in seen:
                    continue

                if not (0 <= nr < R and 0 <= nc < C) or \
                    grid[nr][nc] != selected_color:
                    is_border = True
                    continue

                queue.append((nr, nc))
                seen.add((nr, nc))

            if is_border:
                grid[r][c] = color

        return grid
