#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.22%)
# Total Accepted:    4M
# Total Submissions: 9.9M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        parens = {"(":")", 
                  "[":"]", 
                  "{":"}"}
        
        parens_status = {")":0,
                         "]":0,
                         "}":0}
        
        open_parens=["(", "[", "{"]
        if s[0] not in open_parens:
            return(False)
        if len(s) <=1:
            return(False)
        stack = []
        for p in range(0, len(list(s))-1):
            curr_char = s[p]
            next_char = s[p+1]
            if (curr_char in open_parens):
                stack.append(curr_char)
                parens_status[parens[curr_char]]+=1
                if (next_char not in open_parens) and (parens[curr_char]!=next_char):
                    return(False)
            if (next_char not in open_parens):
                if parens[stack[-1]] != next_char:
                    return(False)
                stack.pop()
                parens_status[next_char]-=1
        if s[-1] in open_parens:
            return(False)
        
        if any([val!=0 for val in parens_status.values()]):
            return(False)
        return(True)
