class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        res = []

        for num in nums2:
            if num not in count or count[num] == 0:
                continue

            res.append(num)
            count[num] -= 1

        return res
