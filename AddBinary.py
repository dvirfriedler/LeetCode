
'''
link - https://leetcode.com/problems/add-binary/description/?envType=study-plan-v2&envId=top-interview-150

Problem: 
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Sultion:

Sultion Approach: Add the bits from right to left and keep track of carry
'''

from typing import List

t = zip([1,2,3],[4,5,6,7,8]) # [(1,4),(2,5),(3,6)]




class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        ans = ""
        
        while i >= 0 or j >=0 or carry ==1:
            
            if i >= 0:
                carry += int(a[i])
                i -= 1
                
            if j >= 0:
                carry += int(b[j])
                j -= 1
                
            ans = str(carry % 2) + ans
            carry = carry // 2
        return ans
            
            
        
                
                
                
        
        
        