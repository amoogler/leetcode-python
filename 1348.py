class TweetCounts:

    def __init__(self):
        self.twitters = collections.defaultdict(list)


    def recordTweet(self, tweetName: str, time: int) -> None:
        self.twitters[tweetName].append(time)


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        timestamps = self.twitters[tweetName]
        secs = 0

        if freq == 'minute':
            secs = 60
        elif freq == 'hour':
            secs = 3600
        elif freq == 'day':
            secs = 86400

        chunk_size = (endTime - startTime) // secs + 1
        res = [0] * chunk_size

        for t in timestamps:
            if startTime <= t <= endTime:
                index = (t - startTime) // secs
                res[index] += 1

        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)