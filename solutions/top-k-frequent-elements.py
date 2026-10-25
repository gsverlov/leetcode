# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        result = []
        for x in nums:
            if not x in hash_map:
                hash_map[x] = 1
            else:
                hash_map[x] = hash_map[x]+1
        
       
        values = list(hash_map.values())
        keys = list(hash_map.keys())
        values = sorted(values)
        values.reverse()
        values2 = list(hash_map.values())
        for x in range(0, k):
            position = values2.index(values[x])
            print(position)
            y = keys[position]
            
            result.append(y)
            values2[position] = -99
          

        return result
