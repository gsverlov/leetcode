# Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)

        for i in range(0, 9):
            for j in range(0, 9):
                value = board[i][j]
                if value == '.':
                    continue
                if value in rows[i]:
                    print("hi")
                    return False
                rows[i].append(value)
                if value in cols[j]:
                    print("hi")
                    return False
                cols[j].append(value)
                box_index = (i//3)*3+(j//3)
                if value in boxes[box_index]:
                    return False
                boxes[box_index].append(value)
                
        print(cols)
        return True
