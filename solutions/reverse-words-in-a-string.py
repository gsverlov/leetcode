# Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        y = ""
        check = 0
        stack = []
        for i in range(0, len(s)):
            if s[i] != " " and check == 0:
                x = i
                check = 1
            if s[i] == " " and check == 1:
                stack.append(s[x:i])
                check = 0
            if i == len(s)-1 and s[i] != " ":
                stack.append(s[x:i+1])
        print(stack)
        for x in range(0, len(stack)-1):
            y = y + stack.pop() + " "
        y = y + stack.pop()
    
        return y
