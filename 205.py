class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1, dict2 = dict(), dict()

        for s_char, t_char in zip(s, t):
            if s_char in dict1:
                if dict1[s_char] != t_char:
                    return False
            else:
                dict1[s_char] = t_char

        for s_char, t_char in zip(s, t):
            if t_char in dict2:
                if dict2[t_char] != s_char:
                    return False
            else:
                dict2[t_char] = s_char

        for key, value in dict1.items():
            if dict2[value] != key:
                return False

        for key, value in dict2.items():
            if dict1[value] != key:
                return False

        return True
