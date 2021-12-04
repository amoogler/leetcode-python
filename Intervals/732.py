class MyCalendarThree:

    def __init__(self):
        self.books = defaultdict(int)
        self.k = 0


    def book(self, start: int, end: int) -> int:
        self.books[start] += 1
        self.books[end] -= 1
        total = 0

        for x in sorted(self.books.keys()):
            total += self.books[x]
            self.k = max(self.k, total)

        return self.k


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
