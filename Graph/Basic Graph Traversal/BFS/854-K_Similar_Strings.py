# Get minimum number of swaps A needs to become B.
#
# We can frame the problem into an undirected graph.
# The node of the graph represents a string.
# The edge of the graph represents that we can change
# vertex on one end to the one in the other end by one swap.
#
# It is a shortest-path problem so we can use BFS.
#
# Note that, list all possible neighbors of A will result in
# TLE. Only neighbors that can make A and B differ less are
# meaningful neighbors.

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        queue = deque([])
        seen = set()
        queue.append(s1)
        seen.add(s1)
        distance = 0

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                node = queue.popleft()

                if node == s2:
                    return distance

                for n in self.getNeighbors(node, s2):
                    if n in seen:
                        continue

                    queue.append(n)
                    seen.add(n)

            distance += 1

        return -1

    def getNeighbors(self, source: str, target: str) -> List[str]:
        res = []
        index = 0
        L = len(source)
        s, t = list(source), list(target)

        # Find the position of first diff.
        while index < L:
            if s[index] != t[index]:
                break

            index += 1

        # Find the position of same char in source compared to original position in target,
        # that is the place we can do a meaningful swap (i.e. make A and B less differ).
        for i in range(index + 1, L):
            if s[i] == t[index]:
                s[i], s[index] = s[index], s[i]
                res.append(''.join(s[:]))
                s[i], s[index] = s[index], s[i]

        return res
