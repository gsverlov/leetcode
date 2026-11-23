# Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for val in asteroids:
            if val < 0 and len(stack) > 0:
                top = stack[len(stack)-1]
                while (top>0 and top < abs(val)) and len(stack)  > 0:
                 
                    stack.pop()
                    
                    if len(stack) != 0:
                        top = stack[len(stack)-1]
                if top == abs(val):
                    stack.pop()
                    continue
                if top >= abs(val) and top > 0:
                    continue     
                
            stack.append(val)
        return stack
