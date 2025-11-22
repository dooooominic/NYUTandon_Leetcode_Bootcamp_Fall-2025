
'''
Homework Assignment 7 (Week 8): Leetcode Bootcamp Section 1 Fall 2025
'''

#Problem 1: Leetcode 416: Partition Equal Subset Sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2 ==1:
            return False #if total sum is odd then can't split

        target = total_sum // 2
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for currSum in range(target, num-1, -1):
                dp[currSum] = dp[currSum] or dp[currSum-num]
        return dp[target]

#Problem 2: Leetcode 322: Coin Change
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float(inf)]*(amount+1) #start with infinite and update with min
        dp[0] = 0 #base case of 0 amount with 0 coin

        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)

        return dp[amount] if dp[amount] != float(inf) else -1

#Problem 3: Leetcode 53: Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0
        for num in nums:
            if total < 0:
                total = 0
            total += num
            res = max(res, total)
        return res
