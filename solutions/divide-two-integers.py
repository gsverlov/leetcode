# Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
       
        count =0

        if dividend == 0:
            return 0
        if divisor < 0:
            Tdivisor = -divisor
        else:
            Tdivisor = divisor
        if dividend < 0:
            Tdividend = -dividend
        else:
            Tdividend = dividend 
        if Tdivisor > Tdividend:
            return 0
        value = Tdivisor
        curr = 1
        while Tdividend >= Tdivisor:
            if Tdividend-value >= 0:
                Tdividend -= value
                count+=curr
                curr +=curr
                value+=value
                
            else:
                value = Tdivisor
                curr = 1
        
        if divisor < 0 and not dividend<0 or dividend<0 and not divisor<0:
            count = -count
        if count >= 2147483648:
            return 2147483647
        if count <= -2147483648:
            return -2147483648
        return count
