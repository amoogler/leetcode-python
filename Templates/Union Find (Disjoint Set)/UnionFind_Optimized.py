class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    # Optimized by path compression.
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    # Optimized by union by rank.
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
                self.root[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Time Complexity
# We tried to balance the tree.
# Union-Find Constructor: O(n)
# Find: O(1) on average.
# Union: O(1) on average as it is based on Find().
# Connected: O(1) on average as it is based on Find().

# Space Complexity
# O(n) for storing the root array and rank array.
