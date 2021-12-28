class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        odd_number = 0

        for frequency in count.values():
            if frequency % 2 == 1:
                odd_number += 1

            if odd_number > 1:
                return False

        return True
