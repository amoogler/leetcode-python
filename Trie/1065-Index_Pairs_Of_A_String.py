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


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        trie = Trie()

        for word in words:
            trie.insert(word)

        for i in range(len(text)):
            node = trie.root

            for j in range(i, len(text)):
                c = text[j]

                if c not in node.children:
                    break
                else:
                    node = node.children[c]

                if node.is_word:
                    res.append([i, j])

        return res
