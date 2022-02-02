class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = defaultdict(list)
        seen = dict()
        heap = [(0, 0, discounts)]

        for u, v, w in highways:
            graph[u].append((v, w))
            graph[v].append((u, w))

        while heap:
            curr_cost, node, curr_discount = heapq.heappop(heap)

            if node in seen and curr_discount <= seen[node]:
                continue

            # For Dijkstra, the first node we visited is the one with minimum cost.
            if node == n - 1:
                return curr_cost

            seen[node] = curr_discount

            for next_node, distance in graph[node]:
                if next_node in seen:
                    continue

                # Add two cases to the heap.
                if curr_discount > 0:
                    heapq.heappush(heap, (curr_cost + distance // 2, next_node, curr_discount - 1))

                heapq.heappush(heap, (curr_cost + distance, next_node, curr_discount))

        return -1
