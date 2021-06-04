class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freqs = Counter(tasks)
        max_freq = max(task_freqs.values())
        max_count = list(task_freqs.values()).count(max_freq)

        interval_count = max_freq - 1
        interval_length = n - (max_count - 1)
        empty_slots = interval_count * interval_length
        left_tasks = len(tasks) - max_freq * max_count
        idles = max(0, empty_slots - left_tasks)

        return len(tasks) + idles
