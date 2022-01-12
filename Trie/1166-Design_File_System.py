class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path: str, value: int) -> bool:
        curr_node = self.root
        dirs = path[1:].split('/')

        for d in dirs[:len(dirs) - 1]:
            if d not in curr_node.children:
                return False
            else:
                curr_node = curr_node.children[d]

        if dirs[-1] in curr_node.children:
            return False
        else:
            curr_node.children[dirs[-1]] = TrieNode()
            curr_node = curr_node.children[dirs[-1]]
            curr_node.value = value
            return True

    def search(self, path: str) -> int:
        curr_node = self.root

        for d in path[1:].split('/'):
            if d not in curr_node.children:
                return None
            else:
                curr_node = curr_node.children[d]

        return curr_node.value

class FileSystem:

    def __init__(self):
        self.trie = Trie()

    def createPath(self, path: str, value: int) -> bool:
        return self.trie.insert(path, value)

    def get(self, path: str) -> int:
        value = self.trie.search(path)
        return value if value else -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
