class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        table = Counter(p)
        l, r, N, count = 0, 0, len(s), len(p)
        res = []

        while r < N:
            if table[s[r]] > 0:
                count -= 1

            table[s[r]] -= 1
            r += 1

            if count == 0:
                res.append(l)

            if r - l == len(p):
                if table[s[l]] >= 0:
                    count += 1

                table[s[l]] += 1
                l += 1

        return res
