class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)

        for equation in equations:
            letter1_off = ord(equation[0]) - ord('a')
            letter2_off = ord(equation[3]) - ord('a')
            operator = equation[1]

            if operator == '=':
                uf.union(letter1_off, letter2_off)

        for equation in equations:
            letter1_off = ord(equation[0]) - ord('a')
            letter2_off = ord(equation[3]) - ord('a')
            operator = equation[1]

            if uf.connected(letter1_off, letter2_off) and operator == '!':
                return False

        return True
