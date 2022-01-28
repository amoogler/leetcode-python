class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

# 1. Every positive integer has a unique prime factorization.
# 2. Every positive integer (except 1) can be decomposed into a series list of prime numbers.
# So rather than enumerating all the factors of a number, we just need to enumerate the prime
# factors of a number, in our UF data structure.
class Solution:
    def primeDecompose(self, num: int) -> List[int]:
        factor = 2
        prime_factors = []

        while num >= factor * factor:
            if num % factor == 0:
                prime_factors.append(factor)
                num //= factor
            else:
                factor += 1

        prime_factors.append(num)
        return prime_factors

    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums) + 1)
        group_count = defaultdict(int)
        num_factor = dict()
        max_size = 0
        group_count = defaultdict(int)

        for num in nums:
            prime_factors = list(set(self.primeDecompose(num)))
            num_factor[num] = prime_factors[0]

            for i in range(0, len(prime_factors) - 1):
                uf.union(prime_factors[i], prime_factors[i + 1])

        for num in nums:
            group_id = uf.find(num_factor[num])
            group_count[group_id] += 1
            max_size = max(max_size, group_count[group_id])

        return max_size
