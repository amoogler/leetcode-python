# Queue based Dijkstra's algorithm solution.
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(set)
        seen = defaultdict(lambda: float('inf'))
        seen[src] = 0
        queue = deque([(src, -1, 0)])

        # Build a weighted directed graph.
        for u, v, w in flights:
            graph[u].add((v, w))

        # Apply Dijkstra's algorithm to find the shortest path from a
        # single source to destination in a weighted directed graph.
        while queue:
            curr_pos, stops, cost = queue.popleft()

            if curr_pos == dst or stops == k:
                continue

            for next_pos, price in graph[curr_pos]:
                new_cost = cost + price

                if new_cost < seen[next_pos]:
                    seen[next_pos] = new_cost
                    queue.append((next_pos, stops + 1, new_cost))

        return seen[dst] if seen[dst] != float('inf') else -1

# Heap based Dijkstra's algorithm solution.
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        heap = [(0, src, -1)]
        seen = defaultdict(int)

        for u, v, w in flights:
            graph[u].append((v, w))

        while heap:
            cost, curr_pos, stops = heapq.heappop(heap)

            if curr_pos == dst:
                return cost

            if stops == k:
                continue

            if curr_pos in seen and seen[curr_pos] < stops:
                continue

            seen[curr_pos] = stops

            for next_pos, price in graph[curr_pos]:
                heapq.heappush(heap, (cost + price, next_pos, stops + 1))

        return -1
