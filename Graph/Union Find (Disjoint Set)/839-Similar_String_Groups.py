# This is a graph problem.
# Find number of connected components in an undirected graph.
# Vertex of the graph is word.
# Edge of the graph means the vertices (words) on both ends are similar.

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
        elif self.rank[root_x] < self.rank[root_y]:
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
    def numSimilarGroups(self, strs: List[str]) -> int:
        L = len(strs)
        uf = UnionFind(L)

        for i in range(L - 1):
            for j in range(i + 1, L):
                if uf.connected(i, j):
                    continue

                if self.isSimilar(strs[i], strs[j]):
                    uf.union(i, j)

        return uf.size()

    def isSimilar(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False

        if str1 == str2:
            return True

        diff = [(a, b) for a, b in zip(str1, str2) if a != b]
        return len(diff) == 2 and diff[0] == diff[1][::-1]
