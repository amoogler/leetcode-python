from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total_pairs = 0
        
        for count in Counter(nums).values():
            if count > 1:
                total_pairs += math.comb(count, 2)
        
        return total_pairs
