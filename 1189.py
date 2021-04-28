class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        def ok(letter_count: Counter) -> bool:
            return letter_count['b'] >= 1 and \
                   letter_count['a'] >= 1 and \
                   letter_count['l'] >= 2 and \
                   letter_count['o'] >= 2 and \
                   letter_count['n'] >= 1

        letter_count = Counter(text)
        max_num = 0

        while ok(letter_count):
            for letter in "balloon":
                letter_count[letter] -= 1

            max_num += 1

        return max_num
