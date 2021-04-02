from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        
        for idx, num in enumerate(nums):
            if num != 0:
                nums[idx], nums[start] = nums[start], nums[idx]
                start += 1
