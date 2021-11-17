class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res, N = [], len(currentState)

        if N < 2:
            return res

        for i in range(1, N):
            if currentState[i] == '+' and currentState[i - 1] == '+':
                state = list(currentState)
                state[i] = '-'
                state[i - 1] = '-'
                res.append(''.join(state))

        return res
