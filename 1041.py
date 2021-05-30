class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))
        x, y = 0, 0
        face = 0

        for instruction in instructions:
            if instruction == 'L':
                face = (face + 3) % 4
            elif instruction == 'R':
                face = (face + 1) % 4
            else:
                x += DIR[face][0]
                y += DIR[face][1]

        return face != 0 or (x == 0 and y == 0)
