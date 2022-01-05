class Solution:
    def maximumSwap(self, num: int) -> int:
        number= list(str(num))
        indice_table = defaultdict(int)

        for i, c in enumerate(number):
            indice_table[c] = i

        for i, c in enumerate(number):
            for d in range(9, int(c), -1):
                if indice_table[str(d)] > i:
                    number[i], number[indice_table[str(d)]] = number[indice_table[str(d)]], number[i]
                    return int(''.join(number))

        return num
