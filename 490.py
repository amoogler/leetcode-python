# class Solution:
#     def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
#         self.R, self.C = len(maze), len(maze[0])
#         visited = [[False] * self.C for _ in range(self.R)]

#         return self.dfs(maze, start, destination, visited)

#     def dfs(self, maze: List[List[int]], start: List[int], destination: List[int], visited: List[List[int]]) -> bool:
#         sr, sc = start[0], start[1]

#         if visited[sr][sc]:
#             return False

#         if sr == destination[0] and sc == destination[1]:
#             return True

#         visited[sr][sc] = True
#         up, down, left, right = sr - 1, sr + 1, sc - 1, sc + 1

#         while up >= 0 and maze[up][sc] == 0:
#             up -= 1

#         if (self.dfs(maze, [up + 1, sc], destination, visited)):
#             return True

#         while down < self.R and maze[down][sc] == 0:
#             down += 1

#         if (self.dfs(maze, [down - 1, sc], destination, visited)):
#             return True

#         while left >= 0 and maze[sr][left] == 0:
#             left -= 1

#         if (self.dfs(maze, [sr, left + 1], destination, visited)):
#             return True

#         while right < self.C and maze[sr][right] == 0:
#             right += 1

#         if (self.dfs(maze, [sr, right - 1], destination, visited)):
#             return True

#         return False
# DFS solution.


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        R, C = len(maze), len(maze[0])
        visited = [[False] * C for _ in range(R)]
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        queue = deque([start])
        visited[start[0]][start[1]] = True

        while queue:
            sr, sc = queue.popleft()

            if sr == destination[0] and sc == destination[1]:
                return True

            for dr, dc in DIRS:
                new_r, new_c = sr + dr, sc + dc

                while new_r >= 0 and new_r < R and new_c >= 0 and new_c < C and maze[new_r][new_c] == 0:
                    new_r += dr
                    new_c += dc

                if not visited[new_r - dr][new_c - dc]:
                    queue.append([new_r - dr, new_c - dc])
                    visited[new_r - dr][new_c - dc] = True

        return False
