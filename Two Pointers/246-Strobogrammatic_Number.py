class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        table = {
            '6' : '9',
            '9' : '6',
            '1' : '1',
            '0' : '0',
            '8' : '8'
        }

        start, end = 0, len(num) - 1

        while start <= end:
            if num[start] not in table or num[end] not in table:
                return False

            if table[num[start]] != num[end]:
                return False

            start += 1
            end -= 1

        return True
