class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []

        for i, c in enumerate(s):
            if i % 2 == 0:
                res.append(c)
            else:
                res.append(chr(ord(s[i - 1]) + ord(c) - ord('0')))

        return ''.join(res)
