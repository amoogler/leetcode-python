# This problem is asking how many connected components in the grid.
# The definition of the connected component is a group of stones with
# either same x or same y axis.
# Union find based solution.

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

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

        self.count -= 1

    def log(self):
        return self.count

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        uf = UnionFind(N)

        for i in range(N - 1):
            for j in range(i + 1, N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)

        return N - uf.log()
