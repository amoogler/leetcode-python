class Solution:
    def countEven(self, num: int) -> int:
        count = 0

        for i in range(1, num + 1):
            if self.getDigitSum(i):
                count += 1

        return count

    def getDigitSum(self, num) -> bool:
        digit_sum = 0

        while num > 0:
            digit_sum += (num % 10)
            num //= 10

        return digit_sum % 2 == 0
