'''
Homework Assignment 2: Leetcode Bootcamp Section 1 Fall 2025
'''

#Problem 1: #8: String to Integer
class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = "0123456789"
        if not s:
            return 0

        digit = 0
        n = len(s)
        sign = 1

        while digit < n and s[digit] == " ":
            digit += 1
        
        if digit < n and s[digit] == "-":
            sign = -1
            digit += 1 
        elif digit< n and s[digit]=="+":
            sign = 1
            digit += 1
        
        result = 0
        while digit < n and s[digit] in numbers:
            result = result*10 + int(s[digit])
            if result * sign > 2**31-1:
                return 2**31-1
            elif result * sign < -(2**31):
                return -(2**31)
            digit+=1
        return result * sign
    
#Problem 2: #151: Reverse words in string
class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()
        i = 0
        j = len(words)-1
        while i < j:
            words[i],words[j] = words[j],words[i]
            i+=1
            j-=1
        return " ".join(words)
    
#Problem 3: #438: Find all anagrams in a string
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        dic = defaultdict(int)
        ans = defaultdict(int)
        res = []
        for c in p:
            dic[c]+=1

        for c in s[:len(p)]:
            ans[c]+=1
        if ans == dic:
            res.append(0)

        left = 0
        for right in range(len(p),len(s)):
            ans[s[right]] += 1
            ans[s[left]] -= 1
            if ans[s[left]] == 0:
                del ans[s[left]]

            left+=1 
            if ans == dic:
                res.append(left)
        return res