# DFS based solution.
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(target: str, pr: int, pc: int, r: int, c: int) -> bool:
            visited.add((r, c))

            # Recursive steps.
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < R and 0 <= nc < C) or \
                    (nr, nc) == (pr, pc) or \
                    grid[nr][nc] != target: \
                    continue

                if (nr, nc) in visited:
                    return True
                elif dfs(target, r, c, nr, nc):
                    return True

            return False

        R, C = len(grid), len(grid[0])
        visited = set()
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        for i in range(R):
            for j in range(C):
                if (i, j) in visited:
                    continue

                if dfs(grid[i][j], -1, -1, i, j):
                    return True
        return False
