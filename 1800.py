from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        slow = 0
        subarray_sum = nums[slow]
        max_sum = subarray_sum

        for fast in range(1, len(nums)):
            if nums[fast] > nums[fast - 1]:
                subarray_sum += nums[fast]
                max_sum = max(subarray_sum, max_sum)
            else:
                slow = fast
                subarray_sum = nums[slow]
                
        return max_sum
        