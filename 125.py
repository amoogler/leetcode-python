class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [char.lower() for char in s if char.isalnum()]
        start, end = 0, len(letters) - 1

        while start < end:
            if letters[start] != letters[end]:
                return False

            start += 1
            end -= 1

        return True
