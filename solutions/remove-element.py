# Remove Element
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for value in nums:
            if value == val:
                count+=1
        for i in range(count):
            nums.remove(val)
