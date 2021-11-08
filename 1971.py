class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        seen, graph = set(), defaultdict(list)

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        queue = deque([start])

        while queue:
            curr = queue.pop()

            if curr == end:
                return True
            elif curr in graph and curr not in seen:
                queue.extend(graph[curr])
                seen.add(curr)

        return False
