# Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = nums[0]
        second = 2147483647
        for i in range(0, len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
               

            #print("smallest")
            #print(smallest)
            if nums[i] < second and nums[i] > smallest:
                second = nums[i]
            #print("second")
            #print(second)
            if nums[i] > second:
                #print(nums.index(second))
                return True
       
        #print(smallest)
        #print(second)
        #print("hello")
        return False
