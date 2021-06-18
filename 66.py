class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i] + carry

            if digit > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = digit
                carry = 0

        if carry == 1:
            return [1] + digits

        return digits
