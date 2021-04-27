class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letter_count = Counter(text)
        max_num = 0

        while 1:
            for letter in "balloon":
                if letter_count[letter] > 0:
                    letter_count[letter] -= 1
                else:
                    return max_num

            max_num += 1
