# Removing Stars From a String
# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "*":
                stack.append(char)
            else:
                stack.pop()
        print(stack)
        answer = ""
        for val in stack:
            answer += val
        return answer
