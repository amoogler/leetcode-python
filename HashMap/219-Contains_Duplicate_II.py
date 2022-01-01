class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = dict()

        for idx, num in enumerate(nums):
            if num in table and abs(table[num] - idx) <= k:
                return True

            # index will be updated to the latest one that gurantees shortest distance.
            table[num] = idx

        return False
