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

    def searchRoot(self, word: str) -> str:
        root = []
        curr_node = self.root

        for c in word:
            if c in curr_node.children:
                root.append(c)
                curr_node = curr_node.children[c]

                if curr_node.is_word:
                    return ''.join(root)
            else:
                break

        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        trie = Trie()
        res = []

        for root in dictionary:
            trie.insert(root)

        for word in words:
            res.append(trie.searchRoot(word))

        return ' '.join(res)
