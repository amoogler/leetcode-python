class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n > 0:
            num = n & 1
            
            if num == 1:
                count += 1
                
            n >>= 1
            
        return count
 