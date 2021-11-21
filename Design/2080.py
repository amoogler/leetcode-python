class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.map = defaultdict(list)

        for i, num in enumerate(arr):
            self.map[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.map:
            return 0

        return bisect.bisect_right(self.map[value], right) - bisect.bisect_left(self.map[value], left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
