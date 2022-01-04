class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Pre-processing given word list and build a graph in adjacency list form.
        # One vertex of the graph represents one word (e.g. dog or dig).
        # One edge of the graph represents two words differed by one letter (e.g. dog -> d*g <- dig).
        L = len(beginWord)
        graph = defaultdict(list)

        for word in wordList:
            for i in range(L):
                graph[word[:i] + '*' + word[i + 1:]].append(word)

        # Now, the problem turns into find the shortest path from source vertex to
        # destination vertex in an undirected graph. Do via BFS.
        queue = deque([beginWord])
        seen = set()
        seen.add(beginWord)
        distance = 1

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                word = queue.popleft()

                for i in range(L):
                    transformed_word = word[:i] + '*' + word[i + 1:]

                    for w in graph[transformed_word]:
                        if w in seen:
                            continue

                        if w == endWord:
                            return distance + 1

                        seen.add(w)
                        queue.append(w)

            distance += 1

        return 0
