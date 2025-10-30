from typing import List
from collections import defaultdict

'''
Homework Assignment 4: Leetcode Bootcamp Section 1 Fall 2025
'''

#Problem 1: Leetcode 232. Implement Queue using Stacks
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


#Problem 2: Leetcode 739. Daily Temperatures

class Solution: #I've done this one before. Using Monotonic stack, storing indices in stack.
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ans[j] = i-j
            stack.append(i)
        
        return ans


#Problem 3: Leetcode 2327. Number of People Aware of a Secret
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        knows = [0]*n #list of n days, each entry is # of new people learning the secret that day
        knows[0] = 1 #person 1 knows
        shared = 0 #how many people can share
        total = 1 #how many people still remember and haven't forgotten

        for day in range(delay,forget):
            shared += knows[day-delay] # number of people who can share on this day after the delay
            total += shared #all the new people still remember as of today
            knows[day] = shared #number of people who
        
        for day in range(forget, n):
            shared += knows[day - delay] - knows[day - forget]
            total += shared - knows[day - forget]
            knows[day] = shared
        
        return total % 1000000007