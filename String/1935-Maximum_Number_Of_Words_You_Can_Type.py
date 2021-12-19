class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_list = text.split(" ")
        broken = set()
        res = 0

        for letter in brokenLetters:
            broken.add(letter)

        for word in text_list:
            if all(ch not in broken for ch in word):
                res += 1

        return res
