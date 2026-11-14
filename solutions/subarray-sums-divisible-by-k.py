# Subarray Sums Divisible by K
# https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
      hash = {0: 1}
      answer = 0
      pre_sum = 0
      for n in nums:
        pre_sum = pre_sum + n
        if pre_sum % k in hash:
            answer += hash[pre_sum%k]
            hash[pre_sum%k] = 1+hash[pre_sum%k]
        else:
            hash[pre_sum%k] = 1
        print(pre_sum)
      return answer
