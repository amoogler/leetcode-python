class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree, courses = [0] * numCourses, []
        queue = deque()

        # Build an adjacency list to represent directed graph.
        for c, p in prerequisites:
            graph[p].append(c)
            indegree[c] += 1

        # Implement Kahn's algorithm to find topological ordering.
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            courses.append(course)

            for v in graph[course]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    queue.append(v)

        return courses if len(courses) == numCourses else []
