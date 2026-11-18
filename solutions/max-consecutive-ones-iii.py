# Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes = 0
        leftindex = 0
        rightindex = 0
        first = 0
        total = 0
        total1 = 0

        while rightindex < len(nums):
            if nums[rightindex] == 0:
                zeroes +=1
            if zeroes == k+1:
                if nums[leftindex] == 0:
                    leftindex = leftindex+1
                else:
                    while nums[leftindex] != 0:
                        leftindex = leftindex + 1
                    leftindex = leftindex + 1
                zeroes -=1
            rightindex = rightindex+ 1
            total = rightindex - leftindex 
            if total > total1:
                total1 = total
      
        
        return total1
