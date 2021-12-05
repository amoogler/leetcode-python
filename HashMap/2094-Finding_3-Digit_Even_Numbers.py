class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        self.count = Counter(digits)
        res = []

        for num in range(100, 1000):
            if num % 2 == 1:
                continue

            if self.found(num):
                res.append(num)

        return res

    def found(self, num: int) -> bool:
        table = self.count.copy()

        while num > 0:
            digit = num % 10

            if digit not in table or table[digit] == 0:
                return False

            table[digit] -= 1
            num //= 10

        return True
