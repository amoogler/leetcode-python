class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.space_size = 9999
        self.space = [[] for _ in range(self.space_size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashcode = key % self.space_size

        for idx, [k, v] in enumerate(self.space[hashcode]):
            if k == key:
                self.space[hashcode][idx] = [key, value]
                return

        self.space[hashcode].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashcode = key % self.space_size

        for k, v in self.space[hashcode]:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashcode = key % self.space_size

        for k, v in self.space[hashcode]:
            if k == key:
                self.space[hashcode].remove([k, v])

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
