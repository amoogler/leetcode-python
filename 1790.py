class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        pairs = []
        
        for idx, (e1, e2) in enumerate(zip(s1, s2)):
            if e1 != e2:
                pairs.append([e1, e2])
                
                if len(pairs) > 2:
                    return False
                
        if not pairs:
            return True
        
        if len(pairs) == 1:
            return False
                
        return pairs[0][0] == pairs[1][1] and pairs[0][1] == pairs[1][0]
