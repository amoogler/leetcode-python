# If we find the presum % k was seen at an earlier index,
# we know there is an continuous subarray sums to be a
# multiple of k.
#
# We need two handles to fullfill the requirements:
# 1. Make sure the subarray with length >= 2.
# 2. presum % k == 0, so initialize map with 0 (presum % k): -1 (index).
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        presum = 0

        for i, num in enumerate(nums):
            presum += num
            presum %= k

            if presum in d:
                if i - d[presum] > 1:
                    return True
            else:
                d[presum] = i

        return False
