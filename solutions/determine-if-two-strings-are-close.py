# Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        map = {}
        map2 = {}
        total = 0
        set1 = set()
        set2 = set()
        list1= []
        list2= []
        if len(word1) != len(word2):
            return False
        for char in word1:
            if char in map:
                map[char] = map[char] + 1
            else:
                map[char] =1
        for char in word2:
            if char in map2:
                map2[char] = map2[char] + 1
            else:
                map2[char] =1
        for val in map:
            set1.add(map[val])
            list1.append(map[val])
        for val in map2:
             set2.add(map2[val])
             list2.append(map2[val])
        print(list1)
        print(list2)
        if set1 == set2 and Counter(list1) == Counter(list2):
            for num in word2:
                if num in map:
                    total+=1
        if total == len(word2):
            return True

        print(list1)
        return False
