# Find similarity is same as to find if there is a path between two nodes in an undirected graph.

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        self.graph = defaultdict(list)

        # Build an adjacency list to represent an undirected graph.
        for x, y in similarPairs:
            self.graph[x].append(y)
            self.graph[y].append(x)

        return all(self.isSimilar(w1, w2) for w1, w2 in zip(sentence1, sentence2))

    def isSimilar(self, word1: str, word2: str) -> bool:
        if word1 == word2:
            return True

        queue = deque([word1])
        seen = set()
        seen.add(word1)

        while queue:

            word = queue.popleft()

            if word == word2:
                return True

            for w in self.graph[word]:

                if w not in seen:
                    queue.append(w)
                    seen.add(w)

        return False
