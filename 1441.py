class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []

        for i in range(1, target[-1] + 1):
            res.append("Push")

            if i not in target:
                res.append("Pop")

        return res