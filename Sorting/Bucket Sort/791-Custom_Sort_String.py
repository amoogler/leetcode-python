class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []

        count = Counter(s)

        for c in order:
            if c in count:
                while count[c] > 0:
                    res.append(c)
                    count[c] -= 1

        for c in count:
            while count[c] > 0:
                res.append(c)
                count[c] -= 1

        return ''.join(res)
