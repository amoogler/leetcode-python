class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n

        for pe, ne in relations:
            graph[pe - 1].append(ne - 1)
            indegree[ne - 1] += 1

        queue = deque([])
        dp = [0] * n

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i] = time[i]

        while queue:
            u = queue.popleft()

            for v in graph[u]:
                dp[v] = max(dp[u] + time[v], dp[v])
                indegree[v] -= 1

                if indegree[v] == 0:
                    queue.append(v)

        return max(dp)
