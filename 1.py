from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        dictionary = dict()
        
        for idx, num in enumerate(nums):
            if target - num in dictionary.keys():
                ans = [dictionary[target - num], idx]
            else:
                dictionary[num] = idx
        
        return ans
 