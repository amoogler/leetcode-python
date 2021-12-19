class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        sorted_words = []
        cleaned_words = []
        word = []

        for c in paragraph:
            if c.isalpha():
                word.append(c.lower())
            else:
                if word:
                    cleaned_words.append(''.join(word))
                    word = []

        if word:
            cleaned_words.append(''.join(word))

        sorted_words = Counter(cleaned_words).most_common()
        banned_set = set(banned)

        for word, frequency in sorted_words:
            if word not in banned_set:
                return word
