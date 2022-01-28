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

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        uf = UnionFind(N)
        res = []

        # Build connected components.
        for x, y in pairs:
            uf.union(x, y)

        # Build a sorted list of chars for each component.
        chars = defaultdict(list)

        for i in range(N):
            chars[uf.find(i)].append(s[i])

        for value in chars.values():
            value.sort()

        # Find the belonged component and take the lowest char.
        for i in range(N):
            res.append(chars[uf.find(i)][0])
            del chars[uf.find(i)][0]

        return ''.join(res)
