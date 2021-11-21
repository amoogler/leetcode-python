class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        N = len(colors)
        res = 0

        for i, j in product(range(N), range(N)):
            if colors[i] != colors[j]:
                res = max(res, abs(i - j))

        return res
