# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        pre = 1
        suff = 1
        for i in range(0, len(nums)):
            answer[i] = pre 
            pre = pre * nums[i]
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i]*suff
            suff = suff * nums[i]
    
        return answer
