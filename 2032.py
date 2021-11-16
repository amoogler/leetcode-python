class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dictionary = defaultdict(set)

        for n1 in nums1:
            dictionary[n1].add(1)

        for n2 in nums2:
            dictionary[n2].add(2)

        for n3 in nums3:
            dictionary[n3].add(3)

        return [k for k, v in dictionary.items() if len(v) >= 2]
