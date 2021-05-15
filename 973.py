import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, res = [], []

        for x, y in points:
            distance = pow(x, 2) + pow(y, 2)
            heapq.heappush(heap, (distance, [x, y]))

        elements = heapq.nsmallest(k, heap)

        for distance, point in elements:
            res.append(point)

        return res
