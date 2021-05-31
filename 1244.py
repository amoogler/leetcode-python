class Leaderboard:

    def __init__(self):
        self.score_board = collections.defaultdict(int)


    def addScore(self, playerId: int, score: int) -> None:
        self.score_board[playerId] += score


    def top(self, K: int) -> int:
        scores = heapq.nlargest(K, self.score_board.values())
        return sum(scores)


    def reset(self, playerId: int) -> None:
        self.score_board[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)