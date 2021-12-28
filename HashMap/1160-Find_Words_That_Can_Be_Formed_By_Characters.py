class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        for word in words:
            count_word = Counter(word)

            if all(count_word[c] <= count[c] for c in count_word):
                res += len(word)

        return res
