class Solution:
    def interpret(self, command: str) -> str:
        final_string = ""
        
        if command[0] is 'G':
            final_string += 'G'
        
        for i in range(1, len(command)):
            if command[i] is 'G':
                final_string += 'G'
            elif command[i] is ')':
                if command[i - 1] is '(':
                    final_string += 'o'
                elif command[i - 1] is 'l':
                    final_string += 'al'
        
        return final_string
