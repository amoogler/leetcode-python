# BFS Solution.
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        d = defaultdict(list)
        d[0].append([0, firstPerson])
        res = {0, firstPerson}

        for start, end, time in meetings:
            d[time].append([start, end])

        for time in sorted(d.keys()):
            # Only one meeting at this timestamp.
            if len(d[time]) == 1:
                if d[time][0][0] in res or d[time][0][1] in res:
                    res.add(d[time][0][0])
                    res.add(d[time][0][1])

                continue

            # Concurrent meetings at this timestamp,
            # we'll have a un-directed graph.
            self.graph = defaultdict(list)

            for x, y in d[time]:
                self.graph[x].append(y)
                self.graph[y].append(x)

            # Do BFS to traverse the graph and get all
            # non-duplicate, reachable vertices.
            res = self.bfs(res)

        return list(res)

    def bfs(self, secret_keepers: set) -> set:
        queue = deque(secret_keepers)
        people = set()

        while queue:
            person = queue.popleft()
            people.add(person)

            for v in self.graph[person]:
                if v not in people:
                    queue.append(v)

        return people
