class Solution:
    def addDigits(self, num: int) -> int:
        digits_sum = 0

        while num > 0:
            digit = num % 10
            digits_sum += digit
            num //= 10

            if num == 0 and digits_sum > 9:
                num = digits_sum
                digits_sum = 0

        return digits_sum
