class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(' ')
        res = []

        for word in words:
            if len(word) < 3:
                res.append(word.lower())
            else:
                res.append(word[0].upper() + word[1:].lower())

        return ' '.join(res)
