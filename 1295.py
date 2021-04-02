from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for num in nums:
            if self.countDigits(num) % 2 == 0:
                count += 1
        
        return count

    def countDigits(self, num: int) -> int:
        count = 0
        
        while num > 0:
            count += 1
            num //= 10 
        
        return count
