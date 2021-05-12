class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = collections.deque()
        idx, prev_max = len(heights) - 1, 0

        while idx >= 0:
            if heights[idx] > prev_max:
                res.appendleft(idx)

            prev_max = max(heights[idx], prev_max)
            idx -= 1

        return res
