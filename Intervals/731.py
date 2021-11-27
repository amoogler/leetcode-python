class MyCalendarTwo:

    def __init__(self):
        self.books = defaultdict(int)


    def book(self, start: int, end: int) -> bool:
        self.books[start] += 1
        self.books[end] -= 1
        total = 0

        for x in sorted(self.books.keys()):
            total += self.books[x]

            if total > 2:
                self.books[start] -= 1
                self.books[end] += 1
                return False

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
