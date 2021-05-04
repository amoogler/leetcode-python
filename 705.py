# N.B.
# We should go back visit linkedlist and BST solutions.
# We should do time complexity analysis for each HashSet function.

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.SPACE_SIZE = 9999
        self.space = [[] for _ in range(self.SPACE_SIZE)]

    def add(self, key: int) -> None:
        hashcode = self.computeHash(key)

        for k in self.space[hashcode]:
            if key == k:
                return

        self.space[hashcode].append(key)

    def remove(self, key: int) -> None:
        hashcode = self.computeHash(key)

        for k in self.space[hashcode]:
            if key == k:
                self.space[hashcode].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashcode = self.computeHash(key)

        for k in self.space[hashcode]:
            if key == k:
                return True

        return False

    def computeHash(self, key: int) -> int:
        return key % self.SPACE_SIZE


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
