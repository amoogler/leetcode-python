class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = list(word)
        
        for i in range(len(nums)):
            if not nums[i].isnumeric():
                nums[i] = " "

        unique_nums = set(int(num) for num in "".join(nums).split())
        
        return len(unique_nums)
