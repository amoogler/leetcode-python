class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reverted = 0

        while x != 0:
            last_digit = x % 10
            reverted = reverted * 10 + last_digit
            x //= 10

        return original == reverted
