class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split(" ")
        prev_num = None

        for word in words:
            if not word.isdecimal():
                continue

            if prev_num != None:
                if int(word) <= prev_num:
                    return False

            prev_num = int(word)

        return True
