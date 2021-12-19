class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0
        self.word_count = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr_node = self.root

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()

            curr_node = curr_node.children[c]
            curr_node.prefix_count += 1

        curr_node.word_count += 1


    def countWordsEqualTo(self, word: str) -> int:
        curr_node = self.root

        for c in word:
            if c not in curr_node.children:
                return 0
            else:
                curr_node = curr_node.children[c]

        return curr_node.word_count


    def countWordsStartingWith(self, prefix: str) -> int:
        curr_node = self.root

        for c in prefix:
            if c not in curr_node.children:
                return 0
            else:
                curr_node = curr_node.children[c]

        return curr_node.prefix_count


    def erase(self, word: str) -> None:
        curr_node = self.root

        for c in word:
            curr_node = curr_node.children[c]
            curr_node.prefix_count -= 1

        curr_node.word_count -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
