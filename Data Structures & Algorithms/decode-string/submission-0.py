class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        decodedString = ""

        for char in s:
            if char != ']':
                stack.append(char)
            
            else:
                # Get encoded string
                encodedString = ""
                while stack and stack[-1] != '[':
                    encodedString = stack.pop() + encodedString
                
                # Pop opening square bracket in stack
                stack.pop()

                # Get number
                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                
                stack.append(int(number) * encodedString)
        
        while stack:
            decodedString = stack.pop() + decodedString

        return decodedString