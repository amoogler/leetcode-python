class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t

        curr = ord(s[0])

        for c in s[1:]:
            curr ^= ord(c)

        for c in t:
            curr ^= ord(c)

        return chr(curr)
