class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        # Upon s is equal to goal, we need to swap duplicate characters.
        if s == goal and len(set(s)) < len(goal):
            return True

        # In other cases, we should only have 2 diffs for one swap.
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(diff) == 2 and diff[0] == diff[1][::-1]
