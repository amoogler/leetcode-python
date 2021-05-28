class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr_node = self.root

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()

            curr_node = curr_node.children[c]

        curr_node.is_word = True


    def search(self, word: str) -> bool:
        def search_backtrack(word: str, node: TrieNode) -> bool:
            for i, c in enumerate(word):
                if c not in node.children:
                    if c == '.' and any(search_backtrack(word[i + 1:], node.children[x]) for x in node.children):
                        return True
                    return False
                else:
                    node = node.children[c]

            return node.is_word

        return search_backtrack(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
