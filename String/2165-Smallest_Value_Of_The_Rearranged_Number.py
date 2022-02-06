class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        digits = []
        sign = 1 if num > 0 else -1

        if num < 0:
            num = -num

        while num > 0:
            digit = num % 10
            num //= 10
            digits.append(digit)

        digits.sort()

        if sign < 0:
            digits = digits[::-1]

        lead_zeros = 0

        for digit in digits:
            if digit == 0:
                lead_zeros += 1
            else:
                break

        digits = digits[lead_zeros:lead_zeros + 1] + digits[:lead_zeros] + digits[lead_zeros + 1:]
        val = 0

        for digit in digits:
            val *= 10
            val += digit

        return val * sign
