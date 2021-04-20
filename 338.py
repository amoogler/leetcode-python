class Solution:
    def countBits(self, num: int) -> List[int]:
        bit_count = []

        for i in range(0, num + 1):
            count = self.counting(i)
            bit_count.append(count)

        return bit_count

    def counting(self, num: int) -> int:
        count = 0

        while num > 0:
            if num & 1 == 1:
                count += 1

            num >>= 1

        return count
