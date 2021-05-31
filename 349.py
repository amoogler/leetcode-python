class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        res = set()

        for num in nums2:
            if num in s1:
                res.add(num)

        return res

# Other conditions:
# lists are already sorted
# O(1) space complexity