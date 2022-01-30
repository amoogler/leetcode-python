class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        # Build a directed graph and indegree map.
        for word in words:
            for c in word:
                indegree[c] = 0

        for i in range(len(words) - 1):
            # Invalid order.
            if len(words[i]) > len(words[i + 1]) and words[i].startswith(words[i + 1]):
                return ""

            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].append(words[i + 1][j])
                    indegree[words[i + 1][j]] += 1
                    break

        queue = deque([])
        res = []

        for letter, value in indegree.items():
            if value == 0:
                queue.append(letter)

        while queue:
            curr = queue.popleft()
            res.append(curr)

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # No valid topological order.
        if len(res) != len(indegree):
            return ""

        return ''.join(res)
