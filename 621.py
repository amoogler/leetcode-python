class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freqs = Counter(tasks)
        sorted_freqs = sorted(task_freqs.values(), reverse=True)

        max_freq, max_count = sorted_freqs[0], 1

        for freq in sorted_freqs[1:]:
            if freq == max_freq:
                max_count += 1
            else:
                break

        part_count = max_freq - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        left_task_slots = len(tasks) - max_freq * max_count
        idles = max(0, empty_slots - left_task_slots)

        return len(tasks) + idles
