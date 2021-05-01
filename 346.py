class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = collections.deque()
        self.num_sum = 0
        self.num_count = 0

    def next(self, val: int) -> float:
        self.num_sum += val
        self.num_count += 1
        self.queue.append(val)

        if self.num_count > self.size:
            self.num_sum -= self.queue.popleft()

        return self.num_sum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
