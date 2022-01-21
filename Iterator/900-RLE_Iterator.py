class RLEIterator:

    def __init__(self, A: List[int]):
        self.arr = A

    def next(self, n: int) -> int:
        while self.arr:
            while self.arr and self.arr[0] == 0:
                # Remove the head of list if count is 0.
                self.arr.pop(0)
                self.arr.pop(0)

            if self.arr:
                if n <= self.arr[0]:
                    self.arr[0] -= n
                    return self.arr[1]
                else:
                    n -= self.arr[0]
                    self.arr[0] = 0

        return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
