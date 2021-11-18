# Find if the graph is a DAG (directed acyclic graph).

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, indegree = defaultdict(list), [0] * numCourses
        queue = deque()
        count = 0

        # Build adjacency list to represent a directed graph and indegree array.
        for c, p in prerequisites:
            graph[p].append(c)
            indegree[c] += 1

        # Implementation of Kahn's algorithm.
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            count += 1

            for v in graph[course]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    queue.append(v)

        return count == numCourses
