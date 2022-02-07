class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x : x[0])
        merged = []
        current = sorted_intervals[0]

        for incoming_start, incoming_end in sorted_intervals[1:]:
            current_start = current[0]
            current_end = current[1]

            if incoming_start > current_end:
                merged.append(current)
                current = [incoming_start, incoming_end]
            else:
                current = [current_start, max(current_end, incoming_end)]

        merged.append(current)

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
