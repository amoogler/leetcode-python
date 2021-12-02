class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 32

        while count > 0:
            rightmost_bit = n & 1
            res = res * 2 + rightmost_bit
            n >>= 1
            count -= 1

        return res
