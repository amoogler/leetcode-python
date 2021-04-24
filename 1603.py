class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lots = dict()
        self.lots[1] = big
        self.lots[2] = medium
        self.lots[3] = small

    def addCar(self, carType: int) -> bool:
        if self.lots[carType] <= 0:
            return False
        else:
            self.lots[carType] -= 1
            return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
