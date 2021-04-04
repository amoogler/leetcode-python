class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_to_mins = defaultdict(set)
        ans_arr = [0] * k

        for user, minute in logs:
            user_to_mins[user].add(minute)
        print(user_to_mins)
        for minutes in user_to_mins.values():
            ans_arr[len(minutes) - 1] += 1
        
        return ans_arr
