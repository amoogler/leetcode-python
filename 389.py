class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t

        curr = ord(s[0]) - ord('a')

        for c in s[1:]:
            curr ^= ord(c) - ord('a')

        for c in t:
            curr ^= ord(c) - ord('a')

        return chr(ord('a') + curr)
