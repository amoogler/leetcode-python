class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct_strs = []
        count = Counter(arr)

        for key, value in count.items():
            if value == 1:
                distinct_strs.append(key)

        return distinct_strs[k - 1] if len(distinct_strs) >= k else ""
