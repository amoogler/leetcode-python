class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        seen, graph = set(), defaultdict(list)

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        queue = deque([start])
        seen.add(start)

        while queue:
            curr = queue.pop()

            if curr == end:
                return True

            for v in graph[curr]:
                if v not in seen:
                    queue.append(v)
                    seen.add(v)

        return False
