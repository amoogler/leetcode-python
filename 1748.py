from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        table = dict()
        sum_unique = 0
        
        for num in nums:
            if num in table.keys():
                table[num] += 1
            else:
                table[num] = 1
        
        for key, value in table.items():
            if value == 1:
                sum_unique += key
        
        return sum_unique
  