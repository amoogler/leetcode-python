class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.root[root_y] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Time Complexity
# Union-Find Constructor: O(n)
# Find: O(n) in worst case.
# Union: O(n) in worst case as it is based on Find(); however, quicker than Quick-Find.
# Connected: O(n) in worst case as it is based on Find().

# Space Complexity
# O(n) for storing the root array. Index is the vertex and value is the parent vertex.
