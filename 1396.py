class UndergroundSystem:

    def __init__(self):
        self.check_ins = dict()
        self.total_times = collections.defaultdict(list)


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.total_times[(self.check_ins[id][0], stationName)].append(t - self.check_ins[id][1])


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.total_times[(startStation, endStation)]
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)