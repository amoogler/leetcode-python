class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        step = 0
        next_steps = defaultdict(list)
        next_steps['0'].extend(['9', '1'])
        next_steps['9'].extend(['8', '0'])

        for i in range(1, 9):
            next_steps[str(i)].extend([str(i - 1), str(i + 1)])

        if '0000' in deadends:
            return -1

        queue = deque(['0000'])
        seen = {'0000'}

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                curr_num = queue.popleft()

                if curr_num == target:
                    return step

                for i in range(4):
                    for next_step in next_steps[curr_num[i]]:
                        next_num = list(curr_num)
                        next_num[i] = next_step
                        next_num = ''.join(next_num)

                        if next_num in deadends or next_num in seen:
                            continue

                        queue.append(next_num)
                        seen.add(next_num)

            step += 1

        return -1
