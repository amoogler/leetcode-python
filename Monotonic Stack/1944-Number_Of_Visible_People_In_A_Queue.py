class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        N = len(heights)
        res = [0] * N
        stack = []

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                res[stack.pop()] += 1

            if stack:
                res[stack[-1]] += 1

            stack.append(i)

        return res
