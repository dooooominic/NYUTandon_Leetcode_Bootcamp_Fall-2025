from typing import List

'''
Homework Assignment 6 (Week 7): Leetcode Bootcamp Section 1 Fall 2025
'''

#Problem 1: Leetcode 199: Binary Tree Right Side View
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque([root])

        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                #we want last one on each level
                if i == level_size - 1:
                    ans.append(node.val)
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans



#Problem 2: Leetcode 994: Rotting Oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        q= deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] ==2: #rotten
                    q.append((i,j,0))
                if grid[i][j] ==1:
                    fresh +=1

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        maxtime = 0
        rotten = 0

        while q: #bfs with deque
            row, column, t = q.popleft()
            maxtime = max(maxtime, t)

            for dr, dc in directions:
                new_row = row + dr
                new_col = column + dc
                if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] ==1:
                    grid[new_row][new_col] = 2 #rot spreads here
                    q.append((new_row,new_col, t+1)) #add to deque with all rotten oranges
                    rotten +=1
        
        return maxtime if rotten == fresh else -1

#Problem 3: Leetcode 210: Course Schedule II
#will have to review and restudy this again
from collections import defaultdict, deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []