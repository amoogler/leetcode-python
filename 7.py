class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        neg = False

        if x < 0:
            neg = True
            x *= -1

        while x != 0:
            last_digit = x % 10
            res = res * 10 + last_digit
            x //= 10

        if neg:
            res *= -1

        if res < -2 ** 31 or res > 2 **31 - 1:
            return 0

        return res
