# Brute force solution. Time complexity: O(n), Space complexity: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1

        for _ in range(n):
            ans *= x

        return ans

# Faster recursive solution. Time complexity: O(logn), Space complexity: O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x, n):
            if n == 0:
                return 1.0

            half = fastPow(x, n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            x = 1 / x
            n = -n

        return fastPow(x, n)

# Faster iterative solution. Time complexity: O(logn), Space complexity: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        curr_product = x
        i = n

        while i > 0:
            if i % 2 == 1:
                ans = ans * curr_product

            curr_product *= curr_product
            i //= 2

        return ans
