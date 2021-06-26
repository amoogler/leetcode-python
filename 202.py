class Solution:
    def isHappy(self, n: int) -> bool:
        met = set()

        while n != 1:
            number = 0

            while n != 0:
                digit = n % 10
                n //= 10
                number += digit ** 2

            if number in met:
                return False

            met.add(number)
            n = number

        return True
