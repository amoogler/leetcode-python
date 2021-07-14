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
