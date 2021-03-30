from typing import List
from collections import defaultdict

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        table = defaultdict(lambda: 0)
        sum_unique = 0
        
        for num in nums:
            table[num] += 1
        
        for key, value in table.items():
            if value == 1:
                sum_unique += key
        
        return sum_unique
