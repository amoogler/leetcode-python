class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size # The height of each vertex.

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Time Complexity
# We tried to balance the tree.
# Union-Find Constructor: O(n)
# Find: O(logn).
# Union: O(logn) as it is based on Find().
# Connected: O(logn) as it is based on Find().

# Space Complexity
# O(n) for storing the root array. Index is the vertex and value is the parent vertex.
