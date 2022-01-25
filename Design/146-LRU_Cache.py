# OrderedDict based solution. (LinkedHashmap in Java)
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]


    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)

        self[key] = value

        if len(self) > self.capacity:
            self.popitem(last = False)

# Doubly linked list node.
class Node:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    def _add_node(self, node: Node):
        """
        Add new node right to head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        """
        Remove a node from linkedlist.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node: Node):
        """
        Move a node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        node = self.tail.prev
        self._remove_node(node)
        return node

    def __init__(self, capacity: int):
        self.cache = dict()
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = Node(), Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self._move_to_head(self.cache[key])

        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self._move_to_head(self.cache[key])
        else:
            node = Node()
            node.key = key
            node.value = value

            self.cache[key] = node
            self._add_node(node)

            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
