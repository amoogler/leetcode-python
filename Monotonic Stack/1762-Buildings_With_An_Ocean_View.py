class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        higher_idx = [-1] * len(heights)
        stack = []
        res = []

        for idx, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                higher_idx[stack.pop()] = idx

            stack.append(idx)

        for idx, next_higher in enumerate(higher_idx):
            if next_higher == -1:
                res.append(idx)

        return res
