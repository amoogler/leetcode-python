class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(permutation: List[int]):
            if len(permutation) == len(nums):
                permutations.append(permutation[:])
            else:
                for num in nums:
                    if num in permutation:
                        continue
                    else:
                        permutation.append(num)
                        backtrack(permutation)
                        permutation.pop()

        permutations = []
        backtrack([])
        return permutations
