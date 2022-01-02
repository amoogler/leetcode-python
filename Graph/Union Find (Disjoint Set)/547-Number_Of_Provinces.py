# Union Find Solution
class UnionFind:
    def __init__(self):
        self.root = {}
        self.rank = {}
        self.count = 0

    def add(self, x):
        if x in self.root or x in self.rank:
            return

        self.root[x] = x
        self.rank[x] = 1
        self.count += 1

    def size(self):
        return self.count

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_y] < self.rank[root_x]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

            self.count -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        R, C = len(isConnected), len(isConnected[0])
        uf = UnionFind()

        for i, j in product(range(R), range(C)):
            if isConnected[i][j] == 1:
                uf.add(i)
                uf.add(j)
                uf.union(i, j)

        return uf.size()
