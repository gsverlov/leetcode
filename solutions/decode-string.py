# Decode String
# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        total = ""
        for char in s:
            number = "1"
            if char != "]":
                stack.append(char)
            else:
                answer = ""
                while stack[-1] != "[":
                    answer = stack.pop() + answer
                stack.pop()
                number = ""
                while stack and stack[-1].isdigit():
                
                    number = stack.pop() + number
                stack.append(int(number) * answer)
        result = ""
        print(stack)
        for i in range(0, len(stack)):
            result += stack[i]
        return result
