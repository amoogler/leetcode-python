class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = []
        num = []
        
        word = list(word)
        
        for i in range(len(word)):
            if not word[i].isnumeric():
                word[i] = " "

        unique_nums = set(int(num) for num in "".join(word).split())
        
        return len(unique_nums)
