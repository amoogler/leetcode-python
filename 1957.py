class Solution:
    def makeFancyString(self, s: str) -> str:
        N = len(s)

        if N <= 2:
            return s

        s_list = []
        s_list.append(s[0])
        s_list.append(s[1])

        for i in range(2, N):
            if s[i] == s[i - 1] == s[i - 2]:
                continue
            else:
                s_list.append(s[i])

        return ''.join(s_list)
