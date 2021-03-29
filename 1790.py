class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        pairs = []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                pairs.append([s1[i], s2[i]])
                
                if len(pairs) > 2:
                    return False
                
        if not pairs:
            return True
        
        if len(pairs) == 1:
            return False
                
        return True if pairs[0][0] == pairs[1][1] and pairs[0][1] == pairs[1][0] else False   
