'''
Homework Assignment 1: Leetcode Bootcamp Section 1 Fall 2025
'''


#Problem 1: Two pointers 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        curr = left = 0
        right = len(numbers)-1
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left+1, right+1]
            elif curr > target:
                right -= 1
            else:
                left += 1
        return []
    

#Problem 2: Important prefix and suffix product!
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix and suffix product problem, avoid O(n^2) by keeping prefix and suffix at every step
        ans = [1]*len(nums)
        pref = suff = 1
        for i in range(len(nums)):
            ans[i] *= pref
            pref *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suff
            suff *= nums[i]
        return ans
    

#Problem 3: I was only able to come up with this two-pass solution.
from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = defaultdict(int)
        for num in nums:
            counts[num] +=1 

        ind = 0
        for _ in range(counts[0]):
            nums[ind] = 0
            ind += 1
        for _ in range(counts[1]):
            nums[ind] = 1
            ind += 1
        for _ in range(counts[2]):
            nums[ind] = 2
            ind += 1
        return 
            