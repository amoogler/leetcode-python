class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = collections.deque([])
        carry, p1, p2 = 0, len(num1) - 1, len(num2) - 1

        while p1 >= 0 and p2 >= 0:
            x1 = ord(num1[p1]) - ord('0')
            x2 = ord(num2[p2]) - ord('0')
            res.appendleft(str((x1 + x2 + carry) % 10))
            carry = (x1 + x2 + carry) // 10
            p1 -= 1
            p2 -= 1

        while p1 >= 0:
            x1 = ord(num1[p1]) - ord('0')
            res.appendleft(str((x1 + carry) % 10))
            carry = (x1 + carry) // 10
            p1 -= 1

        while p2 >= 0:
            x2 = ord(num2[p2]) - ord('0')
            res.appendleft(str((x2 + carry) % 10))
            carry = (x2 + carry) // 10
            p2 -= 1

        if carry > 0:
            res.appendleft(str(carry))

        return ''.join(res)
