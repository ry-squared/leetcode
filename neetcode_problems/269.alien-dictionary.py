#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#
# https://leetcode.com/problems/alien-dictionary/description/
#
# algorithms
# Hard (35.54%)
# Total Accepted:    359.8K
# Total Submissions: 1M
# Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
#
# There is a new alien language that uses the English alphabet. However, the
# order of the letters is unknown to you.
# 
# You are given a list of strings words from the alien language's dictionary.
# Now it is claimed that the strings in words are sorted lexicographically by
# the rules of this new language.
# 
# If this claim is incorrect, and the given arrangement of string in words
# cannot correspond to any order of letters, return "".
# 
# Otherwise, return a string of the unique letters in the new alien language
# sorted in lexicographically increasing order by the new language's rules. If
# there are multiple solutions, return any of them.
# 
# 
# Example 1:
# 
# 
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# 
# 
# Example 2:
# 
# 
# Input: words = ["z","x"]
# Output: "zx"
# 
# 
# Example 3:
# 
# 
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.
# 
# 
#
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
