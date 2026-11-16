# Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        leftindex = 0
        rightindex = len(nums)-1
        answer = 0
        nums = sorted(nums)
        while leftindex < rightindex:
            val = nums[leftindex] + nums[rightindex]
            if val > k:
                rightindex = rightindex-1
            if val < k:
                leftindex = leftindex +1
            if val == k:
                leftindex = leftindex+1
                rightindex = rightindex-1
                answer +=1
        return answer
