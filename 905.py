class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1

        while i < j:
            if A[i] % 2 == 1 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]

            while A[i] % 2 == 0 and i < j:
                i += 1

            while A[j] % 2 == 1 and i < j:
                j -= 1

        return A
