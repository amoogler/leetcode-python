# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         R, C = len(matrix), len(matrix[0])
#         res = [[0] * C for _ in range(R)]

#         for i in range(R):
#             for j in range(C):
#                 if matrix[i][j] != 0:
#                     res[i][j] = self.distanceToZero(matrix, i, j)

#         return res

#     def distanceToZero(self, matrix: List[List[int]], row: int, col: int):
#         R, C = len(matrix), len(matrix[0])
#         queue = deque([(row, col)])
#         distance = 0

#         while queue:
#             queue_length = len(queue)

#             for _ in range(queue_length):
#                 r, c = queue.popleft()

#                 if matrix[r][c] == 0:
#                     return distance

#                 if r - 1 >= 0:
#                     queue.append((r - 1, c))

#                 if r + 1 < R:
#                     queue.append((r + 1, c))

#                 if c - 1 >= 0:
#                     queue.append((r, c - 1))

#                 if c + 1 < C:
#                     queue.append((r, c + 1))

#             distance += 1

#         return distance
#
# Time Limit Exceeded

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        R, C = len(matrix), len(matrix[0])
        res = [[float('inf')] * C for _ in range(R)]
        queue = deque([])

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))

        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            r, c = queue.popleft()

            for dr, dc in DIRS:
                new_r, new_c = r + dr, c + dc

                if new_r < 0 or new_c < 0 or new_r >= R or new_c >= C or \
                    res[new_r][new_c] != float('inf'):
                    continue

                res[new_r][new_c] = res[r][c] + 1
                queue.append((new_r, new_c))

        return res
