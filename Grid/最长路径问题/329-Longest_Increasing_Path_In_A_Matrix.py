class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longest = 0
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = set()

        @lru_cache(None)
        def dfs(r, c):
            curr_length = 0

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < R and 0 <= nc < C):
                    continue

                if (nr, nc) in visited:
                    continue

                if matrix[r][c] >= matrix[nr][nc]:
                    continue

                visited.add((nr, nc))
                curr_length = max(curr_length, dfs(nr, nc))
                visited.remove((nr, nc))

            return curr_length + 1

        R, C = len(matrix), len(matrix[0])

        for i in range(R):
            for j in range(C):
                visited.add((i, j))
                longest = max(longest, dfs(i, j))
                visited.remove((i, j))

        return longest
