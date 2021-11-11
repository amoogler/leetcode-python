# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
#         seen, graph = set(), defaultdict(list)

#         for s, e in edges:
#             graph[s].append(e)
#             graph[e].append(s)

#         queue = deque([start])
#         seen.add(start)

#         while queue:
#             curr = queue.popleft()

#             if curr == end:
#                 return True

#             for v in graph[curr]:
#                 if v not in seen:
#                     queue.append(v)
#                     seen.add(v)

#         return False

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        seen, graph = set(), defaultdict(list)

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        def dfs(node, end, seen):
            if node == end:
                return True

            if node in seen:
                return False

            seen.add(node)

            for v in graph[node]:
                if dfs(v, end, seen):
                    return True

            return False

        return dfs(start, end, seen)
