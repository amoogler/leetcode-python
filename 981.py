class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = collections.defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        left, right = 0, len(values)

        while left < right:
            mid = left + (right - left) // 2

            if values[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1

        return "" if right == 0 else values[right - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)