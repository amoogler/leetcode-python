# Sweep-line technique solution.
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        total = 0
        res = []

        for a, b in firstList + secondList:
            d[a] += 1
            d[b] -= 1

        for x in sorted(d.keys()):
            prev = total
            total += d[x]

            if prev < 2 and total == 2:
                res.append([x, x])
            elif prev == 2 and total < 2:
                res[-1][-1] = x
            elif prev == 1 and total == 1:
                res.append([x, x])

        return res
