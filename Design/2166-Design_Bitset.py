class Bitset:

    def __init__(self, size: int):
        self.bs = ['0'] * size
        self.zeros = size
        self.ones = 0
        self.size = size
        self.flipped = -1

    def fix(self, idx: int) -> None:
        if self.flipped == -1:
            if self.bs[idx] == '0':
                self.bs[idx] = '1'
                self.ones += 1
                self.zeros -= 1
        else:
            if self.bs[idx] == '1':
                self.bs[idx] = '0'
                self.ones += 1
                self.zeros -= 1

    def unfix(self, idx: int) -> None:
        if self.flipped == -1:
            if self.bs[idx] == '1':
                self.bs[idx] = '0'
                self.ones -= 1
                self.zeros += 1
        else:
            if self.bs[idx] == '0':
                self.bs[idx] = '1'
                self.ones -= 1
                self.zeros += 1

    def flip(self) -> None:
        self.flipped *= -1
        self.ones, self.zeros = self.zeros, self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        if self.flipped == 1:
            for i in range(len(self.bs)):
                if self.bs[i] == '0':
                    self.bs[i] = '1'
                else:
                    self.bs[i] = '0'

            self.flipped = -1

        return ''.join(self.bs)



# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()