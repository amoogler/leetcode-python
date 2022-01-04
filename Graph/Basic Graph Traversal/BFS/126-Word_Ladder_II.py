class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        L = len(beginWord)
        graph = defaultdict(list)

        for word in wordList:
            for i in range(L):
                graph[word[:i] + '*' + word[i + 1:]].append(word)

        queue = deque([(beginWord, [beginWord])])
        seen = set()
        seen.add(beginWord)
        res = []

        while queue:
            queue_length = len(queue)
            # bot -> hot -> cot, bot -> dot -> cot is valid,
            # so we cannot add cot to global set before finishing current level.
            new_nodes = set()
            found = False

            for _ in range(queue_length):
                word, path = queue.popleft()

                for i in range(L):
                    transformed_word = word[:i] + '*' + word[i + 1:]

                    for w in graph[transformed_word]:

                        if w in seen:
                            continue

                        if w == endWord:
                            path.append(endWord)
                            res.append(path[:])
                            path.pop()
                            found = True
                            continue

                        new_nodes.add(w)
                        path.append(w)
                        queue.append((w, path[:]))
                        path.pop()

            # Found the shortest paths, bail early.
            if found:
                return res

            seen.update(new_nodes)

        return res
