# Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        map = []
        map2 = []
        prefix = 0
        for i in range (n):
            prefix = prefix + nums[i]
            map.append(prefix)
        print(map)
        prefix = 0
        for i in range (n-1, -1, -1):
            prefix = prefix + nums[i]
            map2.append(prefix)
        map2.reverse()
        print(map2)
        
        for i in range(n):
            if map[i] == map2[i]:
                return i
     
        return -1
