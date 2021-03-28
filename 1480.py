from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre_sum = 0
        res = []
        
        for i in range(len(nums)):
            pre_sum += nums[i]
            res.append(pre_sum)
        
        return res
