class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits_sum, digits_product = 0, 1

        while n > 0:
            digit = n % 10
            digits_sum += digit
            digits_product *= digit
            n //= 10

        return digits_product - digits_sum
