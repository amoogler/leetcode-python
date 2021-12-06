class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0       
        num = x ^ y
        
        while num > 0:
            bit = num & 1
            
            if bit == 1:
                distance += 1
            
            num >>= 1
            
        return distance
