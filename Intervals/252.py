# Sorting solution.
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x : x[0])

        for i1, i2 in zip(sorted_intervals, sorted_intervals[1:]):
            if i2[0] < i1[1]:
                return False

        return True

# Sweep-line algorithm.
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        d = defaultdict(int)
        total = 0

        for start, end in intervals:
            d[start] += 1
            d[end] -= 1

        for time in sorted(d.keys()):
            total += d[time]

            if total > 1:
                return False

        return True
