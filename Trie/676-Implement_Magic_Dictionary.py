class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()

            curr_node = curr_node.children[c]

        curr_node.is_word = True

class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def find(self, node: TrieNode, word: str, count: int) -> bool:
        if count < 0:
            return False

        if not word:
            return count == 0 and node.is_word

        for c, next_node in node.children.items():
            if word[0] == c:
                if self.find(next_node, word[1:], count):
                    return True
            else:
                if self.find(next_node, word[1:], count - 1):
                    return True

        return False

    def search(self, searchWord: str) -> bool:
        return self.find(self.trie.root, searchWord, 1)



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
