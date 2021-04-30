class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        length_words = collections.defaultdict(list)
        res = []
        words[0] = words[0].lower()

        for word in words:
            length_words[len(word)].append(word)

        sorted_length = sorted(length_words.keys())
        first_word = list(length_words[sorted_length[0]][0])
        first_word[0] = first_word[0].upper()
        length_words[sorted_length[0]][0] = ''.join(first_word)

        for length in sorted_length:
            for word in length_words[length]:
                res.append(word)

        return ' '.join(res)
