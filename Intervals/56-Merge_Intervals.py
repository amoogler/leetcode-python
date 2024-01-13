class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x : x[0])
        merged = []
        curr = sorted_intervals[0]
        for start, end in sorted_intervals[1:]:
            curr_start, curr_end = curr[0], curr[1]
            if start > curr_end:
                merged.append(curr)
                curr = [start, end]
            else:
                curr = [curr_start, max(curr_end, end)]
        merged.append(curr)

        return merged

# Sweep-line technique
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        total = 0
        res = []

        for s, e in intervals:
            d[s] += 1
            d[e] -= 1

        for x in sorted(d.keys()):
            prev = total
            total += d[x]

            if prev == 0 and total > 0:
                res.append([x, x])
            elif prev > 0 and total == 0:
                res[-1][1] = x
            elif prev == 0 and total == 0:
                res.append([x, x])

        return res
