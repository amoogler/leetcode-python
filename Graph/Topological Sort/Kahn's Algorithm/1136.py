class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n
        queue = deque()
        course_count, semester_count = 0, 0

        # Build an adjacency list to represent graph.
        for pre, nxt in relations:
            graph[pre - 1].append(nxt - 1)
            indegree[nxt - 1] += 1

        # Implement Kahn's algorithm.
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            queue_length = len(queue)
            semester_count += 1

            for _ in range(queue_length):
                course = queue.popleft()
                course_count += 1

                for v in graph[course]:
                    indegree[v] -= 1

                    if indegree[v] == 0:
                        queue.append(v)

        return semester_count if course_count == n else -1
