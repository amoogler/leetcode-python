from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        dictionary = dict()
        
        for i in range(len(nums)):
            if target - nums[i] in dictionary.keys():
                ans = [dictionary[target - nums[i]], i]
            else:
                dictionary[nums[i]] = i
        
        return ans
