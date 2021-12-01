# Sweep-line technique solution.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        d = defaultdict(int)
        total = 0
        res = []

        for start, end in intervals:
            d[start] += 1
            d[end] -= 1

        d[newInterval[0]] += 1
        d[newInterval[1]] -= 1

        for x in sorted(d.keys()):
            prev = total
            total += d[x]

            if prev == 0 and total > 0:
                res.append([x, x])
            elif prev > 0 and total == 0:
                res[-1][-1] = x
            elif prev == 0 and total == 0:
                res.append([x, x])

        return res
