# Concise math solution.
# Assume we already have n - 1 pairs, and we need to insert the nth pair.
# To insert the first element, there are 2n - 2 + 1 = 2n - 1 choices.
# To insert the second element, there are 2n - 2 + 1 + 1 = 2n choices.
# Considering delivery(i) always happens after pickup(i), we need to
# devide by 2.
# So it is (2n - 1) * n

class Solution:
    def countOrders(self, n: int) -> int:
        res = 1

        for i in range(1, n + 1):
            res *= i * (2 * i - 1)

        return res % (pow(10, 9) + 7)
