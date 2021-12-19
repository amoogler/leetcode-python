class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)
        index = 0

        for idx, w in enumerate(word_list):
            if w == ch:
                index = idx
                break

        self.swap(word_list, 0, index)
        return ''.join(word_list)

    def swap(self, word_list: List, start: int, end: int) -> List:
        while start < end:
            word_list[start], word_list[end] = word_list[end], word_list[start]
            start += 1
            end -= 1

        return word_list
