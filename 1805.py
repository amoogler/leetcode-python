class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = []
        num = ''
        for char in word:
            if char.isnumeric():
                num += char
            else:
                if len(num) > 0:
                    nums.append(num)
                num = ''
        
        if len(num) > 0:
            nums.append(num)

        unique_nums = set()
        
        for num in nums:
            num = num.lstrip('0')
            unique_nums.add(num)
        
        return len(unique_nums)
