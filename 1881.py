class Solution:
    def maxValue(self, n: str, x: int) -> str:
        n_list = list(n)

        if n_list[0] == '-':
            for i in range(1, len(n_list)):
                if x < int(n_list[i]):
                    n_list.insert(i, str(x))
                    return ''.join(n_list)
        else:
            for i in range(0, len(n_list)):
                if x > int(n_list[i]):
                    n_list.insert(i, str(x))
                    return ''.join(n_list)

        n_list.insert(len(n_list), str(x))
        return ''.join(n_list)
