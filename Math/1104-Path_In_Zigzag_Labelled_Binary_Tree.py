class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = deque([])
        node_count = 1
        level = 1

        # Determine the level of the label.
        while label >= node_count * 2:
            node_count *= 2
            level += 1

        # Iterate from the target lable to the root.
        while level > 0:
            res.appendleft(label)
            level_max = 2 ** (level) - 1
            level_min = 2 ** (level - 1)
            label = int((level_max + level_min - label) // 2)
            level -= 1

        return res
