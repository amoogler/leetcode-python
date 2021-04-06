class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        global_max = current_max

        for num in nums[1:]:
            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)

        return global_max
