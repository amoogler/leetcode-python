# Sweep-line technique.
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        d = defaultdict(int)
        total, curr, res = 0, 0, 0

        for birth, death in logs:
            d[birth] += 1
            d[death] -= 1

        for year in sorted(d.keys()):
            total += d[year]

            if total > curr:
                curr = total
                res = year

        return res
