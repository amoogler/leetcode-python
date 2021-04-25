class Solution:
    def sumBase(self, n: int, k: int) -> int:
        digits_sum = 0

        while n > 0:
            digits_sum += n % k
            n //= k

        return digits_sum