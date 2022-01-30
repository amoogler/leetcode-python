class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = defaultdict(list)

        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)

        route = []

        def visit(airport):
            # Keep going until you cannot go further,
            # means you meet the exit, add it as last node.
            while targets[airport]:
                visit(targets[airport].pop())

            route.append(airport)

        visit('JFK')
        return route[::-1]
