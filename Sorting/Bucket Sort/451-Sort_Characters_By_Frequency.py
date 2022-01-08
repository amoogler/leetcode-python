# Count and sort solution. Time: O(nlogn) Space: O(n).
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        freqToChar = defaultdict(list)
        res = []

        for char, freq in count.items():
            freqToChar[freq].append(char)

        for freq in sorted(freqToChar.keys(), reverse=True):
            for char in freqToChar[freq]:
                res.extend(char * freq)

        return ''.join(res)

# Bucket sort.
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        bucket = [''] * (len(s) + 1)
        res = []

        for char, freq in count.items():
            if not bucket[freq]:
                bucket[freq] = [char]
            else:
                bucket[freq].append(char)

        for i in range(len(bucket) - 1, -1, -1):
            for char in bucket[i]:
                res.extend(char * i)

        return ''.join(res)
