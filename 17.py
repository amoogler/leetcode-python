class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(combination: List[str], digit_idx: int):
            if digit_idx == len(digits):
                combinations.append(''.join(combination[:]))
                return

            for letter in phone_pad[int(digits[digit_idx])]:
                combination.append(letter)
                backtrack(combination, digit_idx + 1)
                combination.pop()

        if not digits:
            return []

        phone_pad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        combinations = []
        backtrack([], 0)
        return combinations
