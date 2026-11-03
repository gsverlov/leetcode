# 3Sum
# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        answer = []
        for x in range(len(nums) - 2):
            i = nums[x]
            left, right = x+1, len(nums) - 1
            while left < right:
                total = i + nums[left] + nums[right]
                if total == 0 :
                    result = [i, nums[left], nums[right]]
                    result.sort()
                    if result not in answer:
                        answer.append([i, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return answer

    

        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
