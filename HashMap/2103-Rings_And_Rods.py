class Solution:
    def countPoints(self, rings: str) -> int:
        table = defaultdict(set)
        res = 0

        for i in range(0, len(rings), 2):
            table[rings[i + 1]].add(rings[i])

        for value in table.values():
            if len(value) == 3:
                res += 1

        return res
