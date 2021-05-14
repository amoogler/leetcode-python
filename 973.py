import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, res = [], []

        for point in points:
            x, y = point[0], point[1]
            distance = pow(x, 2) + pow(y, 2)
            heapq.heappush(heap, (distance, point))

        elements = heapq.nsmallest(k, heap)

        for e in elements:
            res.append(e[1])

        return res
