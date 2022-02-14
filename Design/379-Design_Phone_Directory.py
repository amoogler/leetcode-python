class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.bool_array = [True] * maxNumbers
        self.queue = deque([i for i in range(maxNumbers)])
        self.max_numbers = maxNumbers

    def get(self) -> int:
        if not self.queue:
            return -1

        value = self.queue.popleft()
        self.bool_array[value] = False
        return value

    def check(self, number: int) -> bool:
        if number >= self.max_numbers:
            return False

        return self.bool_array[number]

    def release(self, number: int) -> None:
        if number >= self.max_numbers:
            return

        if self.bool_array[number]:
            return

        self.bool_array[number] = True
        self.queue.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
