class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        xor = x ^ y
        while xor:
            if xor & 1 == 1:
                distance += 1
            xor >>= 1

        return distance
