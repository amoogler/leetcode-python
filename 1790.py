class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diff = [(e1, e2) for e1, e2 in zip(s1, s2) if e1 != e2]
                
        return diff[0] == diff[1][::-1] if len(diff) == 2 else False
