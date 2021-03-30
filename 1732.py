from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        pre_sum = 0
        sum_list = []
        sum_list.append(highest)
        
        for num in gain:
            pre_sum += num
            sum_list.append(pre_sum)

        highest = max(sum_list)
        
        return highest
