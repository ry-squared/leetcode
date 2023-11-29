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

        paren_stack = []
        open_parens = ["(", "[", "{"]
        for i in range(len(s)):

            if s[i] in open_parens:
                paren_stack.append(s[i])
            else:
                if paren_stack ==[]:
                    return(False)
                stack_top = paren_stack.pop()
                if s[i]==")":
                    if stack_top != "(":
                        return(False)
                if s[i]=="]":
                    if stack_top != "[":
                        return(False)
                if s[i]=="}":
                    if stack_top != "{":
                        return(False)
        
        if len(paren_stack) > 0:
            return(False)
            
        return(True)