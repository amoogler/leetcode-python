class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = (False, None)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()

            curr_node = curr_node.children[c]

        curr_node.is_word = (True, word)

    def build(self, words: List[str]) -> None:
        for word in words:
            self.insert(word)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def backtrack(row: int, col: int, curr_trie: 'TrieNode') -> None:
            if curr_trie.is_word[0]:
                res.append(curr_trie.is_word[1])
                curr_trie.is_word = (False, None) # oa oaa

            c = board[row][col]
            board[row][col] = '#'

            for dr, dc in DIRS:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < R and 0 <= nc < C):
                    continue

                if board[nr][nc] not in curr_trie.children:
                    continue

                backtrack(nr, nc, curr_trie.children[board[nr][nc]])

            board[row][col] = c

        res = []
        trie = Trie()
        trie.build(words)
        curr_trie = trie.root

        for i, j in product(range(R), range(C)):
            if board[i][j] in curr_trie.children:
                backtrack(i, j, curr_trie.children[board[i][j]])

        return res
