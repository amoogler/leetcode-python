class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        idx, hay_length, nee_length = 0, len(haystack), len(needle)

        while idx < hay_length and hay_length - idx >= nee_length:
            if all(h == n for h, n in zip(haystack[idx:], needle)):
                return idx

            idx += 1

        return -1
