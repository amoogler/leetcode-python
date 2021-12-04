# Sweep-line technique solution.
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        d = defaultdict(int)
        total = 0
        shared_slots = []

        for start, end in slots1 + slots2:
            d[start] += 1
            d[end] -= 1

        for x in sorted(d.keys()):
            prev = total
            total += d[x]

            if prev < 2 and total == 2:
                shared_slots.append([x, x])
            elif prev == 2 and total < 2:
                shared_slots[-1][-1] = x
            elif prev == 1 and total == 1:
                shared_slots.append([x, x])

        for start, end in shared_slots:
            if end - start < duration:
                continue
            else:
                return [start, start + duration]

        return []
