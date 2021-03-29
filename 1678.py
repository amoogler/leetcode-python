class Solution:
    def interpret(self, command: str) -> str:
        final = []
        
        for i in range(len(command)):
            if command[i] is 'G':
                final.append('G')
            elif command[i] is ')':
                if command[i - 1] is '(':
                    final.append('o')
                elif command[i - 1] is 'l':
                    final.append('al')
        
        return ''.join(final)
