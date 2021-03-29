from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre_sum = 0
        res = []
        
        for num in nums:
            pre_sum += num
            res.append(pre_sum)
        
        return res
