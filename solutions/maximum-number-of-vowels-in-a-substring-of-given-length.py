# Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        leftindex = 0
        rightindex = 0
        val = 0
        total = 0
        answer = 0
        vowels = "aeiou"
        while rightindex < len(s):
            if s[rightindex] in vowels:
                total += 1
            rightindex = rightindex + 1
            if rightindex - leftindex == k:
                if total > answer:
                    answer = total
                if s[leftindex] in vowels:
                    total -= 1
                leftindex = leftindex + 1
        return answer
