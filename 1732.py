from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        pre_sum = 0
        
        for i in range(len(gain)):
            pre_sum += gain[i]
            gain[i] = pre_sum
        
        for g in gain:
            highest = max(highest, g)
        
        return highest
