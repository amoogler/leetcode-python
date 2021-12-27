class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j  = 0, 0
        W_LENGTH, A_LENGTH = len(word), len(abbr)

        while i < W_LENGTH and j < A_LENGTH:
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue

            if not (ord('1') <= ord(abbr[j]) <= ord('9')):
                return False

            start = j

            while j < A_LENGTH and (ord('0') <= ord(abbr[j]) <= ord('9')):
                j += 1

            i += int(abbr[start : j])

        return i == W_LENGTH and j == A_LENGTH
