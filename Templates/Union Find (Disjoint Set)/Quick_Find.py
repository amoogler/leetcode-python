class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Time Complexity
# Union-Find Constructor: O(n)
# Find: O(1)
# Union: O(N)
# Connected: O(1)

# Space Complexity
# O(n) for storing the root array. Index is the vertex and value is the root.
