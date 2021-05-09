class StringIterator:

    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.ptr = 0
        self.curr_ch = ' '
        self.curr_freq = 0

    def next(self) -> str:
        if not self.hasNext():
            return ' '

        if self.curr_freq == 0:
            self.curr_ch = self.compressedString[self.ptr]
            self.ptr += 1

            while self.ptr < len(self.compressedString) and \
                  self.compressedString[self.ptr].isdigit():
                self.curr_freq = self.curr_freq * 10 + ord(self.compressedString[self.ptr]) - ord('0')
                self.ptr += 1

        self.curr_freq -= 1

        return self.curr_ch

    def hasNext(self) -> bool:
        return self.curr_freq > 0 or self.ptr < len(self.compressedString) - 1


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
