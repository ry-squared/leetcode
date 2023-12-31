#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.20%)
# Total Accepted:    757K
# Total Submissions: 1.7M
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of
# s2.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
# 
# 
#
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        #idea: find same length windows where frequencies of letters are the same
        i = 0
        j = len(s1)
        s1_freq = Counter(s1)
        s2_freq = Counter(s2[i:j])

        while j<len(s2):
            if s1_freq == s2_freq:
                return True
            s2_freq[s2[i]]-=1
            s2_freq[s2[j]]+=1
            i+=1
            j+=1
        
        if s1_freq == s2_freq:
            return True
        
        return False
