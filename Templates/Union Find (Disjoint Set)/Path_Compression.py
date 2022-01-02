class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.root[root_y] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Time Complexity
# We tried to balance the tree.
# Union-Find Constructor: O(n)
# Find: O(logn) in average, O(1) in best, O(n) in worst.
# Union: O(logn) as it is based on Find().
# Connected: O(logn) as it is based on Find().

# Space Complexity
# O(n) for storing the root array.
