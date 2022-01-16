class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        res = []

        # Sort the tasks by enqueue time and keep a reference to the index of original tasks list.
        tasks_by_et = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])

        clock = tasks_by_et[0][0]
        idx = 0

        while len(res) < len(tasks_by_et):
            # Push all tasks whose start time <= current clock into heap.
            while idx < len(tasks_by_et) and tasks_by_et[idx][0] <= clock:
                heapq.heappush(heap, (tasks_by_et[idx][1], tasks_by_et[idx][2]))
                idx += 1

            if heap:
                # Pop the first task to be processed.
                pt, original_idx = heapq.heappop(heap)
                clock += pt
                res.append(original_idx)
            elif idx < len(tasks_by_et):
                clock = tasks_by_et[idx][0]

        return res
