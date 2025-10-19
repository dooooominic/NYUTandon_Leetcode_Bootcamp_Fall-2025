from typing import List
from collections import defaultdict

'''
Homework Assignment 3: Leetcode Bootcamp Section 1 Fall 2025
'''

#Problem 1: #234: Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = head
        arr = []
        while dummy is not None:
            arr.append(dummy.val)
            dummy = dummy.next
        i = 0
        j = len(arr)-1
        while i < j:
            if arr[i] != arr[j]:
                return False
            else:
                i+=1
                j-=1
        return True
        

#Problem 2: #143: Reorder List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle
        if not head:
            return []
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half -- all these questions seem to involve this step
        prev = None
        curr = slow.next
        while curr:
            nextt = curr.next #save the next node
            curr.next = prev #reverse
            prev = curr #move on
            curr = nextt
        slow.next = None #separate from second half before merge

        #merge?
        head1 = head
        head2 = prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt

#Problem 3: #73: Set Matrix Zeros
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero = False

        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                zero = True
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0 #set first element of row and column to 0 if there is a zero anywhere
                    matrix[0][col] = 0
            
            
        for row in range(len(matrix)-1, -1, -1):
            for col in range(len(matrix[0])-1, 0, -1):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
            if zero:
                matrix[row][0] = 0
            