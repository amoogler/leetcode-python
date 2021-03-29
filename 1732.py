from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        pre_sum = 0
        sum_list = []
        
        for num in gain:
            pre_sum += num
            sum_list.append(pre_sum)
        
        for s in sum_list:
            highest = max(highest, s)
        
        return highest
