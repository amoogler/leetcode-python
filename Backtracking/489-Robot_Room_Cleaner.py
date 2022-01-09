# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # Going clockwise.
        DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
        visited = set()

        def back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(row: int, col: int, direction: int):
            visited.add((row, col))
            robot.clean()

            for i in range(4):
                nd = (direction + i) % 4
                dr, dc = DIRS[nd][0], DIRS[nd][1]
                nr, nc = row + dr, col + dc

                if (nr, nc) not in visited and robot.move():
                    backtrack(nr, nc, nd)
                    back()

                robot.turnRight()

        backtrack(0, 0, 0)
