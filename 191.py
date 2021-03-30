class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n > 0:
            lsb = n & 1
            
            if lsb == 1:
                count += 1
                
            n >>= 1
            
        return count
 