class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []


    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)


    def pop(self) -> int:
        x = self.stack.pop()

        if x == self.max_stack[-1]:
            self.max_stack.pop()

        return x


    def top(self) -> int:
        return self.stack[-1]


    def peekMax(self) -> int:
        return self.max_stack[-1]


    def popMax(self) -> int:
        max_value = self.max_stack[-1]
        temp = []

        while self.stack:
            value = self.stack.pop()

            if value != max_value:
                temp.append(value)
            else:
                self.max_stack.pop()
                break

        while temp:
            self.push(temp.pop())

        return max_value


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()