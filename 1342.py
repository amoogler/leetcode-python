class Solution:
    def numberOfSteps(self, num: int) -> int:
        total_steps = 0
        
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
        
            total_steps += 1
        
        return total_steps
