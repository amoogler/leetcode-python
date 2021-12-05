"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

# Sweep-line technique solution.
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        employees_num = len(schedule)
        d = defaultdict(int)
        total = 0
        res = [Interval(float('-inf'), float('inf'))]

        for employee in schedule:
            for interval in employee:
                start, end = interval.start, interval.end

                d[start] += 1
                d[end] -= 1

        for x in sorted(d.keys()):
            prev = total
            total += d[x]

            if prev != 0 and total == 0:
                res.append(Interval(x, float('inf')))
            elif prev == 0 and total != 0:
                res[-1].end = x

        return res[1:len(res) - 1]
