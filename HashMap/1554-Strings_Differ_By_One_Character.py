class Solution:
    def differByOne(self, words: List[str]) -> bool:
        hashset = set()

        for word in words:
            for i in range(len(word)):
                regex = word[:i] + '*' + word[i + 1:]

                if regex in hashset:
                    return True
                else:
                    hashset.add(regex)

        return False
