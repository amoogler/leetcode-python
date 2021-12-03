class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = dict()

        for idx, num2 in enumerate(nums):
            num1 = target - num2
            if num1 in dictionary.keys():
                return [dictionary[num1], idx]
            else:
                dictionary[num2] = idx

        return []
