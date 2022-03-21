class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        res = 0
        dig_set = set()

        for r, c in dig:
            dig_set.add((r, c))

        for r1, c1, r2, c2 in artifacts:
            artifact = []

            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dig_set:
                        artifact.append((r, c))

            if len(artifact) == 0:
                res += 1

        return res
