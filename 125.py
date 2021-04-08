import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile('[^a-zA-Z0-9]')
        letter_str = regex.sub('', s).lower()

        start, end = 0, len(letter_str) - 1

        while start < end:
            if letter_str[start] != letter_str[end]:
                return False

            start += 1
            end -= 1

        return True
