class MyCalendar:

    def __init__(self):
        self.d = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.d[start] += 1
        self.d[end] -= 1
        total = 0

        for time in sorted(self.d.keys()):
            total += self.d[time]

            if total > 1:
                self.d[start] -= 1
                self.d[end] += 1
                return False

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)