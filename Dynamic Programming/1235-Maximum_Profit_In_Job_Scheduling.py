# 1. A job cannot be scheduled if a conflicting job has already been scheduled. Each decision made is affected by previous decision.
# 2. Maximum the profit globally.
# Above two are common indicator for using dynamic programming to solve the problem.
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []

        for st, et, pt in zip(startTime, endTime, profit):
            jobs.append((st, et, pt))

        if not jobs:
            return 0

        # Sort jobs by start_time. For each job, we'll try two options.
        # 1. Schedule this job and move on to the next non-conflicting job using binary search.
        # 2. Skip this job and move on to the next available one.
        jobs.sort(key = lambda x:x[1])
        end_list = [e for _, e, _ in jobs]

        # Then, we can make decision about whether we should schedule a job based on which of
        # above two options results in a greater profit.
        # dp[i] represents the max profit we can get from the jobs at index i in jobs list.
        dp = [0] * len(jobs)
        dp[0] = jobs[0][2]

        for i in range(1, len(jobs)):
            st = jobs[i][0] # start_time of a job
            pt = jobs[i][2] # profit of a job

            idx = bisect.bisect_right(end_list, st) - 1
            dp[i] = max(dp[i - 1], (dp[idx] if idx >= 0 else 0) + pt)

        return dp[-1]
