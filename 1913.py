class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[-1] * sorted_nums[-2] - sorted_nums[0] * sorted_nums[1]
