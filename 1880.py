class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def getValue(word: str) -> int:
            value = 0
            pos = 1

            for i in range(len(word) - 1, -1, -1):
                v = (ord(word[i]) - ord('a')) * pos
                value += v
                pos *= 10

            return value

        return getValue(firstWord) + getValue(secondWord) == getValue(targetWord)
