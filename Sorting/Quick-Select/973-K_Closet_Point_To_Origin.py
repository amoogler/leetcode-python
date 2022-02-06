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
        self.quick_select(points, 0, len(points) - 1, k)
        return points[:k]

    def quick_select(self, points, l, r, k):
        if l < r:
            p_rand = random.randint(l, r)
            p = self.partition(points, l, r, p_rand)

            if p == k:
                return
            elif p < k:
                self.quick_select(points, p + 1, r, k)
            else:
                self.quick_select(points, l, p - 1, k)

    def partition(self, points, l, r, p):
        pivot = points[p]
        points[r], points[p] = points[p], points[r]
        le_wall = l

        for i in range(l, r):
            if (points[i][0] ** 2 + points[i][1] ** 2) <= (pivot[0] ** 2 + pivot[1] ** 2):
                points[le_wall], points[i] = points[i], points[le_wall]
                le_wall += 1

        points[le_wall], points[r] = points[r], points[le_wall]
        return le_wall
