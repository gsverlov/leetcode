# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        rightindex = len(height)-1
        leftindex = 0
        area = 0
        while rightindex > leftindex:
            width = rightindex - leftindex
            print(width)
            area1 = width * min(height[rightindex], height[leftindex])
            print(area1)
            if area1 > area:
                area = area1
            if height[rightindex] > height[leftindex]:
                leftindex = leftindex+1
            else:
               rightindex = rightindex-1


        return area
