class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        unique = set()

        for num in counter:
            if counter[num] in unique:
                return False
            else:
                unique.add(counter[num])

        return True
