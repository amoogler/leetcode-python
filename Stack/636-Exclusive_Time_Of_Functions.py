class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            func_idx, action, time = log.split(':')
            func_idx, time = int(func_idx), int(time)

            if action == 'start':
                if stack:
                    res[stack[-1]] += time - prev_time

                stack.append(func_idx)
                prev_time = time
            else:
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return res
