from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total_pairs = 0
        
        for count in Counter(nums).values():
            if count > 1:
                total_pairs += self.countPair(count)
        
        return total_pairs
    
    def countPair(self, count: int) -> int:
        return count * (count - 1) // 2
