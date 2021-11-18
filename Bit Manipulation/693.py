class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_rmb = n & 1

        while n > 0:
            n = n >> 1
            rmb = n & 1

            if prev_rmb ^ rmb == 0:
                return False

            prev_rmb = rmb

        return True
