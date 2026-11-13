# Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer =0
        map = {0: 1}
        prefix_sum = 0
        for n in nums:
            prefix_sum = prefix_sum + n
            diff = prefix_sum - k
            if diff in map:
                answer += map[diff]
            map[prefix_sum] = 1 + map.get(prefix_sum, 0) 
          
        return answer
