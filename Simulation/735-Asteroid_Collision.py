class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # Collision only happens upon current asteroid is left-moving while peak asteroid in stack is right-moving.
            if stack and stack[-1] > 0 and asteroid < 0:
                while stack and stack[-1] > 0 and asteroid < 0:
                    if stack[-1] == -asteroid:
                        stack.pop()
                        asteroid = 0
                        break
                    elif stack[-1] < -asteroid:
                        stack.pop()
                    else:
                        break

                # Left-moving asteroid made all the way through.
                if asteroid != 0 and ((stack and stack[-1] < 0) or not stack):
                    stack.append(asteroid)
            else:
                stack.append(asteroid)

        return stack
