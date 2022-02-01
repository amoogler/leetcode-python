# Use Dijkstra's algorithm to find the shortest path from target to
# all targets.

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        queue = deque([(k, 0)])
        seen = defaultdict(lambda: float('inf'))
        seen[k] = 0
        graph = defaultdict(set)

        for u, v, w in times:
            graph[u].add((v, w))

        while queue:
            curr, cost = queue.popleft()

            for nx, weight in graph[curr]:
                if cost + weight < seen[nx]:
                    seen[nx] = cost + weight
                    queue.append((nx, cost + weight))

        return max(seen.values()) if len(seen) == n else -1

# Heap implementation.
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        heapq.heappush(heap, (0, k))
        seen = defaultdict(lambda: float('inf'))
        seen[k] = 0
        graph = defaultdict(set)

        for u, v, w in times:
            graph[u].add((v, w))

        while heap:
            cost, curr = heapq.heappop(heap)

            for nx, weight in graph[curr]:
                if cost + weight < seen[nx]:
                    seen[nx] = cost + weight
                    heapq.heappush(heap, (cost + weight, nx))

        return max(seen.values()) if len(seen) == n else -1
