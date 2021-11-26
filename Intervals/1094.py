# Sweep-line Solution.
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = defaultdict(int)

        for people, start, end in trips:
            d[start] += people
            d[end] -= people

        total = 0

        for time in sorted(d.keys()):
            total += d[time]

            if total > capacity:
                return False

        return True
