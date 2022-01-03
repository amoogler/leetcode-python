class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

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

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        res = []
        uf = UnionFind(n)

        for u, v in requests:
            root_u, root_v = uf.find(u), uf.find(v)
            approved = True

            if root_u == root_v:
                res.append(approved)
                uf.union(u, v)
                continue

            for x, y in restrictions:
                root_x, root_y = uf.find(x), uf.find(y)

                if (root_u, root_v) == (root_x, root_y) or \
                    (root_u, root_v) == (root_y, root_x):
                    approved = False
                    break

            res.append(approved)

            if approved:
                uf.union(u, v)

        return res
