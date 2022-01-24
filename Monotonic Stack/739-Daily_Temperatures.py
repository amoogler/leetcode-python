# Monotonic stack solution, time complexity: O(n), space complexity: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []
        table = dict()

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                table[stack.pop()] = i

            stack.append(i)

        while stack:
            table[stack.pop()] = None

        for i in range(len(temperatures)):
            if not table[i]:
                res.append(0)
            else:
                res.append(table[i] - i)

        return res

# Optimizing for O(1) space.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0] * N
        hottest = 0

        for curr_day in range(N - 1, -1, -1):
            curr_temp = temperatures[curr_day]

            if curr_temp >= hottest:
                hottest = curr_temp
                continue

            days = 1

            while temperatures[curr_day + days] <= curr_temp:
                days += res[curr_day + days]

            res[curr_day] = days

        return res
