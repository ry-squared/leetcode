#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (34.16%)
# Total Accepted:    5.1M
# Total Submissions: 15M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:



        # 2 pointer- FAST
        substring_hash = {}
        substring_streak = 0
        substring_max_streak = 0
        i=0
        j=0
        while j<len(s):
            current_letter = s[j]
            substring_streak+=1
            if current_letter in substring_hash:
                i=max(substring_hash[current_letter],i) # i is last idx of duplicate letter OR updated i
                substring_streak=j-i
            substring_hash[current_letter]=j
            substring_max_streak = max(substring_max_streak, substring_streak)
            j+=1

        return substring_max_streak



        # # 1 pointer- SLOW
        # s_hash = {}
        # s_count = 0
        # s_max = 0
        # i=0
        # while i<len(s):
        #     if s[i] in s_hash:
        #         i=s_hash[s[i]]
        #         s_hash = {}
        #         s_count = 0
        #     else:
        #         s_hash[s[i]]=i
        #         s_count+=1
        #     s_max = max(s_max, s_count)
        #     i+=1

        # return s_max