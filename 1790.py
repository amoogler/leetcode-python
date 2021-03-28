class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        pairs = []
        count = 0
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                pairs.append([s1[i], s2[i]])
                
                if count > 2:
                    return False
                
        if count == 0:
            return True
        
        if count == 1:
            return False
                
        return True if pairs[0][0] == pairs[1][1] and pairs[0][1] == pairs[1][0] else False
