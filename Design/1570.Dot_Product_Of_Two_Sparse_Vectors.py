class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = dict()

        for idx, num in enumerate(nums):
            if num != 0:
                self.vector[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0

        for key, value in self.vector.items():
            if key in vec.vector:
                ans += value * vec.vector[key]

        return ans


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
