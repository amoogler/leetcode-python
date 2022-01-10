# Graph traversal based solution, results in TLE. Time complexity is O(n ^ 2).
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        min_height = float('inf')
        res = defaultdict(list)

        # Build an adjacency list to represent a graph.
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for i in range(n):
            height = self.getHeight(graph, i)

            if height <= min_height:
                min_height = height
                res[height].append(i)

        return res[min_height]

    def getHeight(self, graph: defaultdict, root: int) -> int:
        queue = deque([root])
        seen = {root}
        height = 0

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                node = queue.popleft()

                for n in graph[node]:
                    if n not in seen:
                        queue.append(n)
                        seen.add(n)

            height += 1

        return height

# Topological sort solution.
# We cannot have more than two centroids in a tree-alike graph.
# The problem is to look for all the centroid nodes in a tree-alike graph (<= 2 of them).
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        graph = defaultdict(list)
        degree = [0] * n
        queue = deque([])

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        remaining = n

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                node = queue.popleft()

                for v in graph[node]:
                    degree[v] -= 1

                    if degree[v] == 1:
                        queue.append(v)

            if remaining - queue_length <= 2:
                break
            else:
                remaining -= queue_length

        return queue
