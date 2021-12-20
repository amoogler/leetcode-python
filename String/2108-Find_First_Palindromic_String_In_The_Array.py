class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word

        return ""

    def isPalindrome(self, word: str) -> bool:
        start, end = 0, len(word) - 1

        while start < end:
            if word[start] != word[end]:
                return False

            start += 1
            end -= 1

        return True
