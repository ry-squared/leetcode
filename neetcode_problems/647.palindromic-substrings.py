#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (68.01%)
# Total Accepted:    642.7K
# Total Submissions: 945K
# Testcase Example:  '"abc"'
#
# Given a string s, return the number of palindromic substrings in it.
# 
# A string is a palindrome when it reads the same backward as forward.
# 
# A substring is a contiguous sequence of characters within the string.
# 
# 
# Example 1:
# 
# 
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# Example 2:
# 
# 
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# 
# 
#
class Solution:
    def countSubstrings(self, s: str) -> int:
        
