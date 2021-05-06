class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count1, count2 = 0, 0
        vowels = set("aeiouAEIOU")

        for c1, c2 in zip(s[0 : len(s) // 2], s[len(s) // 2 : len(s)]):
            if c1 in vowels:
                count1 += 1

            if c2 in vowels:
                count2 += 1

        return count1 == count2
