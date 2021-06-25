class BrowserHistory:

    def __init__(self, homepage: str):
        self.backs = [homepage]
        self.forwards = []


    def visit(self, url: str) -> None:
        self.backs.append(url)
        self.forwards.clear()


    def back(self, steps: int) -> str:
        while len(self.backs) > 1 and steps > 0:
            self.forwards.append(self.backs.pop())
            steps -= 1

        return self.backs[-1]


    def forward(self, steps: int) -> str:
        while len(self.forwards) > 0 and steps > 0:
            self.backs.append(self.forwards.pop())
            steps -= 1

        return self.backs[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)