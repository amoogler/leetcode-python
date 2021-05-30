class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        w2p = dict()
        p2w = dict()

        for w, p in zip(words, pattern):
            if (w in w2p and w2p[w] != p) or (p in p2w and p2w[p] != w):
                return False

            w2p[w] = p
            p2w[p] = w

        return True
