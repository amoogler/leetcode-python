# class Solution:
#     def wallsAndGates(self, rooms: List[List[int]]) -> None:
#         """
#         Do not return anything, modify rooms in-place instead.
#         """
#         self.rooms = rooms
#         self.M, self.N = len(rooms), len(rooms[0])
#         self.INF = 2147483647

#         for i in range(self.M):
#             for j in range(self.N):
#                 if rooms[i][j] == self.INF:
#                     rooms[i][j] = self.distanceToNearestGate(i, j)


#     def distanceToNearestGate(self, start_row: int, start_col: int) -> int:
#         queue = collections.deque([(start_row, start_col)])
#         distance = [[0] * self.N for _ in range(self.M)]
#         DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

#         while queue:
#             row, col = queue.popleft()

#             for dr, dc in DIRS:
#                 r, c = row + dr, col + dc

#                 if r < 0 or r >= self.M or c < 0 or c >= self.N or self.rooms[r][c] == -1 or distance[r][c] != 0:
#                     continue

#                 distance[r][c] = distance[row][col] + 1

#                 if self.rooms[r][c] == 0:
#                     return distance[r][c]

#                 queue.append((r, c))

#         return self.INF

# Time Limit Exceeded.

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        M, N = len(rooms), len(rooms[0])
        EMPTY, GATE = 2147483647, 0
        queue = collections.deque([])

        for i in range(M):
            for j in range(N):
                if rooms[i][j] == GATE:
                    queue.append((i, j))

        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            row, col = queue.popleft()

            for dr, dc in DIRS:
                r, c = row + dr, col + dc

                if r < 0 or r >= M or c < 0 or c >= N or rooms[r][c] != EMPTY:
                    continue

                rooms[r][c] = rooms[row][col] + 1
                queue.append((r, c))
