# Greedy based algorithm.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        curr_end = sorted_intervals[0][1]
        count = 0

        for i in range(1, len(sorted_intervals)):
            # If there is overlapping, remove the one has more impact to later ones.
            if sorted_intervals[i][0] < curr_end:
                count += 1
                curr_end = min(curr_end, sorted_intervals[i][1])
            else:
                curr_end = sorted_intervals[i][1]

        return count
