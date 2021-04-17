class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(permutation: List[int]):
            if len(permutation) == len(nums):
                permutations.append(permutation[:])
            else:
                for i, num in enumerate(sorted_nums):
                    if visited[i] or \
                       (i > 0 and num == sorted_nums[i - 1] and visited[i - 1]):
                        continue
                    else:
                        visited[i] = True
                        permutation.append(num)
                        backtrack(permutation)
                        permutation.pop()
                        visited[i] = False

        sorted_nums = sorted(nums)
        permutations = []
        visited = [False] * len(nums)
        backtrack([])
        return permutations
