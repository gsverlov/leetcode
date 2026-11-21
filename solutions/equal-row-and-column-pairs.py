# Equal Row and Column Pairs
# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        map1 = {}
        map2 = {}
        temp = []
        temp2 = []
        answer = 0
        for i in range(0, len(grid)):
            temp2 = grid[i]
            temp2 = tuple(temp2)
            if temp2 in map1:
                map1[temp2] = map1[temp2]  + 1
            else:
                map1[temp2] = 1
            for j in range(0, len(grid[0])):
                temp.append(grid[j][i])
            temp = tuple(temp)
            if temp in map2:
                map2[temp] = map2[temp]  + 1
            else:
                map2[temp] = 1
            temp = []
            temp2 = []
        for val in map1:
            if val in map2:
                answer += map2[val] * map1[val]
        print(map1)
        print(map2)
        return answer
