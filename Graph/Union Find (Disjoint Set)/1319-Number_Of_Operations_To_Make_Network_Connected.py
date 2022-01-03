class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_y] < self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def size(self):
        return self.count

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        uf = UnionFind(n)
        redundant_cable = 0

        for x, y in connections:
            if uf.connected(x, y):
                redundant_cable += 1
                continue

            uf.union(x, y)

        cluster_count = uf.size()

        if redundant_cable < cluster_count - 1:
            return -1

        return cluster_count - 1
