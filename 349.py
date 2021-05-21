class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        intersections = set()

        while sorted_nums1 and sorted_nums2:
            head1, head2 = sorted_nums1[-1], sorted_nums2[-1]

            if head1 < head2:
                sorted_nums2.pop()
            elif head1 > head2:
                sorted_nums1.pop()
            else:
                intersections.add(head1)
                sorted_nums1.pop()
                sorted_nums2.pop()

        return intersections
