class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphebet = [False] * 26

        for letter in sentence:
            alphebet[ord(letter) - ord('a')] = True

        for letter in alphebet:
            if not letter:
                return False

        return True
