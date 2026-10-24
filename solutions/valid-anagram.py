# Valid Anagram
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        hash_map2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if not s[i] in hash_map:
                hash_map[s[i]] = 1
            else:
                hash_map[s[i]] = hash_map[s[i]] + 1
            if not t[i] in hash_map2:
                hash_map2[t[i]] = 1
            else:
                hash_map2[t[i]] = hash_map2[t[i]] + 1
        return hash_map2 == hash_map
