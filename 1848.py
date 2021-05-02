class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_abs = len(nums)

        for idx, num in enumerate(nums):
            if num == target:
                min_abs = min(min_abs, abs(idx - start))

        return min_abs
