class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_starts = False
        word_length = 0

        for char in reversed(s):
            if not word_starts and char != ' ':
                print(char)
                word_starts = True
                word_length += 1
            elif word_starts and char == ' ':
                break
            elif word_starts:
                word_length += 1

        return word_length
