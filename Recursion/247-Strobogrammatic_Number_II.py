class Solution:
    def __init__(self):
        self.odd_mid = ['0', '1', '8']
        self.even_mid = ['11', '69', '88', '96', '00']

    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return self.odd_mid

        if n == 2:
            return self.even_mid[:-1]

        if n % 2 == 1:
            pre, mid = self.findStrobogrammatic(n - 1), self.odd_mid
        else:
            pre, mid = self.findStrobogrammatic(n - 2), self.even_mid

        pre_mid = (n - 1) // 2

        return [p[:pre_mid] + c + p[pre_mid:] for c in mid for p in pre]
