# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         rows, res = [], []

#         for i in range(len(mat)):
#             rows.append((Counter(mat[i])[1], i))

#         rows = sorted(rows)

#         for row in rows:
#             res.append(row[1])

#         return res[:k]

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binary_search(row: List[int]) -> int:
            left, right = 0, len(row)

            while left < right:
                mid = left + (right - left) // 2

                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid

            return left

        res, heap = [], []

        for idx, row in enumerate(mat):
            heapq.heappush(heap, (binary_search(row), idx))

        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res
