# Heap Solution.
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x : x[0])
        min_heap = []
        heapq.heappush(min_heap, sorted_intervals[0][1])

        for interval in sorted_intervals[1:]:
            if interval[0] >= min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval[1])

        return len(min_heap)

# Sweep-line Solution.
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        d = defaultdict(int)
        min_room, total = 0, 0

        for start, end in intervals:
            d[start] += 1
            d[end] -= 1

        for time in sorted(d.keys()):
            total += d[time]
            min_room = max(min_room, total)

        return min_room
