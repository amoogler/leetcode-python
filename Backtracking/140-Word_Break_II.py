# Trie + Backtracking
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = (False, None)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()

            curr_node = curr_node.children[char]

        curr_node.is_word = (True, word)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()

        for word in wordDict:
            trie.insert(word)

        def backtrack(index, curr):
            if index == len(s):
                res.append(' '.join(curr[:]))
                return

            curr_trie = trie.root

            for i in range(index, len(s)):
                if s[i] not in curr_trie.children:
                    return

                curr_trie = curr_trie.children[s[i]]

                if curr_trie.is_word[0]:
                    curr.append(curr_trie.is_word[1])
                    backtrack(i + 1, curr)
                    curr.pop()

        res = []
        backtrack(0, [])
        return res
