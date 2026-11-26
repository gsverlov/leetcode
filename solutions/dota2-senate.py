# Dota2 Senate
# https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queR = deque()
        queD = deque()
        for i in range(0, len(senate)):
            if senate[i] == "R":
                queR.append(i)
            if senate[i] == "D":
                queD.append(i)
        print(queR)
        print(queD)
        answer = ""
        i=0
        while len(queD) !=0 and len(queR) != 0:
            if queR[0] < queD[0]:
                queD.popleft()
                temp = queR.popleft()
                queR.append(temp+len(senate))
            else:
                queR.popleft()
                temp = queD.popleft()
                queD.append(temp+len(senate))
            i = i+ 1
        print(queR)
        print(queD)
        if len(queR) == 0:
            return "Dire"
        return "Radiant"
