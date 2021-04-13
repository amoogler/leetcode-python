class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        unique = set()

        for num, count in counter.items():
            if count in unique:
                return False
            else:
                unique.add(count)

        return True
