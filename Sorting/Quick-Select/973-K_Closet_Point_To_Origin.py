# Priority queue solution. Time complexity: O(nlogn)
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

# Quick-select solution. Average time complexity: O(n), worst time complexity: O(n ^ 2)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quick_select(points[:], k)

    def quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        low, high = 0, len(points) - 1
        pivot_index = 0

        while pivot_index != k:
            pivot_index = self.partition(points, low, high)

            if pivot_index < k:
                low = pivot_index + 1

                if low > len(points) - 1:
                    return points
            else:
                high = pivot_index - 1

        return points[:pivot_index]

    def partition(self, points: List[List[int]], low: int, high: int) -> int:
        pivot = pow(points[low][0], 2) + pow(points[low][1], 2)
        le_wall = low

        for i in range(low + 1, high + 1):
            distance = pow(points[i][0], 2) + pow(points[i][1], 2)

            if distance <= pivot:
                le_wall += 1
                points[i], points[le_wall] = points[le_wall], points[i]

        points[low], points[le_wall] = points[le_wall], points[low]
        return le_wall
