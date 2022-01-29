# Use slope.
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        if N <= 2:
            return N

        slopes = defaultdict(int)
        res = 0

        for i in range(N):
            slopes.clear()
            overlap, curr_max = 0, 0

            for j in range(i + 1, N):
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]

                if dx == 0 and dy == 0:
                    overlap += 1
                    continue

                slope = dy * 1.0 / dx if dx != 0 else 'inf'
                slopes[slope] += 1
                curr_max = max(curr_max, slopes[slope])

            res = max(res, curr_max + overlap + 1)

        return res
