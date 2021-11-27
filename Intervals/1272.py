class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        d = defaultdict(int)
        total = 0
        res = []

        for start, end in intervals:
            d[start] += 1
            d[end] -= 1

        d[toBeRemoved[0]] -= 1
        d[toBeRemoved[1]] += 1

        for x in sorted(d.keys()):
            prev = total
            total += d[x]

            if prev < 1 and total == 1:
                res.append([x, x])
            elif prev == 1 and total < 1:
                res[-1][-1] = x

        return res
