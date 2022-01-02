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

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

            self.count -= 1

    def size(self):
        return self.count

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        sorted_logs = sorted(logs, key=lambda x:x[0])
        uf = UnionFind(n)

        for timestamp, x, y in sorted_logs:
            uf.union(x, y)

            if uf.size() == 1:
                return timestamp

        return -1
