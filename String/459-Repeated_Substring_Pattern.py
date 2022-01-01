class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)

        for i in range(N // 2, 0, -1):
            if N % i != 0:
                continue

            subs = s[0 : i]
            subs_count = N // i
            builder = []

            for j in range(subs_count):
                builder.append(subs)

            if ''.join(builder) == s:
                return True

        return False
