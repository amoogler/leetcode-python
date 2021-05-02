class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = collections.deque()
        self.num_sum = 0

    def next(self, val: int) -> float:
        self.num_sum += val
        self.queue.append(val)

        if len(self.queue) > self.size:
            self.num_sum -= self.queue.popleft()

        return self.num_sum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
