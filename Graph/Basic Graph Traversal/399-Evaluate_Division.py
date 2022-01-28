# DFS based solution.
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build an adjacency matrix to represent a weighted graph.
        graph = defaultdict(defaultdict)

        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v

        res = []

        def backtrack(curr, target, product, visited):
            visited.add(curr)
            ans = -1.0

            neighbors = graph[curr]

            if target in neighbors:
                ans = product * neighbors[target]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue

                    ans = backtrack(neighbor, target, product * value, visited)

                    if ans != -1.0:
                        break

            visited.remove(curr)
            return ans

        for x, y in queries:
            ans = -1.0

            if x not in graph or y not in graph:
                ans = -1.0
            elif x == y:
                ans = 1.0
            else:
                ans = backtrack(x, y, 1, set())

            res.append(ans)

        return res
