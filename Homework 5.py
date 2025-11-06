from typing import List

'''
Homework Assignment 5 (Week 6): Leetcode Bootcamp Section 1 Fall 2025
'''

#Problem 1: Leetcode 236: Lowest Common Ancestor of a Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right  


#Problem 2: Leetcode 347: Top K Frequent Elements
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        heap = []
        for num in nums:
            dic[num]+=1
        for key, val in dic.items():
            heapq.heappush(heap, (-val, key))
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
            
        return res
