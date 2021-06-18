class MRUQueue:

    def __init__(self, n: int):
        self.mru_queue = collections.deque([i + 1 for i in range(n)])


    def fetch(self, k: int) -> int:
        queue_len = len(self.mru_queue)
        target = None

        for i in range(queue_len):
            num = self.mru_queue.popleft()

            if i + 1 != k:
                self.mru_queue.append(num)
            else:
                target = num

        self.mru_queue.append(target)
        return target


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)