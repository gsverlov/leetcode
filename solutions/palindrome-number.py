# Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        y = str(x)
        h=0
        print(y)
        for z in range(0, len(y)//2):
            if y[z] == y[len(y)-(z+1)]:
                print('hi')
                h = h + 1
        if h == len(y)//2:
            return True
        print(h)
        print((len(y)//2))
        return False
