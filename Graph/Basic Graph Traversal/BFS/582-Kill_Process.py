class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        res = []

        # Build an adjacency list to represent this DAG.
        graph = defaultdict(list)

        for p, pp in zip(pid, ppid):
            graph[pp].append(p)

        queue = deque([kill])

        while queue:
            process = queue.popleft()
            res.append(process)

            for child in graph[process]:
                queue.append(child)

        return res
