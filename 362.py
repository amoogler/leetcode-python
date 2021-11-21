# O(n) for getHits() routine.
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = collections.deque()
        self.total = 0


    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if len(self.hits) == 0 or self.hits[-1][0] != timestamp:
            self.hits.append([timestamp, 1])
        else:
            self.hits[-1][1] += 1

        self.total += 1


    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """

        while self.hits:
            diff = timestamp - self.hits[0][0]

            if (diff >= 300):
                hit = self.hits.popleft()
                self.total -= hit[1]
            else:
                break

        return self.total
