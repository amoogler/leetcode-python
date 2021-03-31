class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        if len(A) == 0 and len(B) == 0:
            return True
        
        length = len(A)
        
        while length > 0:
            length -= 1
            A = A[1:len(A)] + A[0:1]
            
            if A == B:
                return True
        
        return False
