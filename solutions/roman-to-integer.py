# Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I':1,'V':5,"X":10,"L":50, "C":100,"D":500, "M":1000}
        total = 0
        c = -1 
        for char in s:
            c+=1
            value = 0
            value = mapping[char]
            if c + 1 < len(s):
                if value >= mapping[s[c+1]]:
                    total+=value
                else:
                    total-=value
            else:
                total+=value
        return total
